from datetime import datetime
from typing import Any

import httpx

from src.collectors.base import JobCollector
from src.collectors.models import CollectedJob
from src.collectors.company_boards import (
    GREENHOUSE_COMPANIES,
)


class GreenhouseCollector(JobCollector):

    BASE_URL = (
        "https://boards-api.greenhouse.io/v1/boards"
    )

    def __init__(
        self,
        board_token: str,
        timeout: float = 30.0,
    ):

        if not board_token.strip():
            raise ValueError(
                "Greenhouse board token cannot be empty"
            )

        self.board_token = board_token
        self.timeout = timeout

    def fetch_jobs(self) -> list[CollectedJob]:

        url = (
            f"{self.BASE_URL}/"
            f"{self.board_token}/jobs"
        )

        params = {
            "content": "true"
        }

        response = httpx.get(
            url,
            params=params,
            timeout=self.timeout,
        )

        response.raise_for_status()

        data = response.json()

        jobs = data.get("jobs", [])

        return [
            self._normalize_job(job)
            for job in jobs
        ]

    def _normalize_job(
        self,
        job: dict[str, Any],
    ) -> CollectedJob:

        location = job.get("location") or {}

        posted_date = self._parse_datetime(
            job.get("updated_at")
        )

        return CollectedJob(
            source="greenhouse",
            external_job_id=str(job["id"]),
            company=self.board_token,
            title=job.get("title", ""),
            description=job.get("content", ""),
            location=location.get("name"),
            country=None,
            remote_type=None,
            salary_min=None,
            salary_max=None,
            currency=None,
            job_url=job.get("absolute_url", ""),
            posted_date=posted_date,
        )

    @staticmethod
    def _parse_datetime(
        value: str | None,
    ) -> datetime | None:

        if not value:
            return None

        try:

            return datetime.fromisoformat(
                value.replace("Z", "+00:00")
            )

        except ValueError:

            return None

    @classmethod
    def fetch_all_companies(
        cls,
    ) -> list[CollectedJob]:

        all_jobs: list[CollectedJob] = []

        for company_name, board_token in (
            GREENHOUSE_COMPANIES.items()
        ):

            print(
                f"Fetching jobs from {company_name}..."
            )

            try:

                collector = cls(
                    board_token=board_token
                )

                jobs = collector.fetch_jobs()

                print(
                    f"{company_name}: "
                    f"{len(jobs)} jobs found"
                )

                all_jobs.extend(jobs)

            except httpx.HTTPStatusError as error:

                print(
                    f"Failed to fetch {company_name}: "
                    f"HTTP {error.response.status_code}"
                )

            except httpx.RequestError as error:

                print(
                    f"Network error for {company_name}: "
                    f"{error}"
                )

        return all_jobs


if __name__ == "__main__":

    jobs = GreenhouseCollector.fetch_all_companies()

    print(
        f"\nTotal jobs collected: {len(jobs)}"
    )

    for job in jobs[:5]:

        print(
            job.company,
            "|",
            job.title,
            "|",
            job.location,
        )