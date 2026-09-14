from datetime import datetime

import httpx

from .base import JobCollector
from .models import CollectedJob


REMOTIVE_API_URL = "https://remotive.com/api/remote-jobs"


class RemotiveCollector(JobCollector):

    def __init__(self, timeout: float = 30.0):
        self.timeout = timeout

    def fetch_jobs(self) -> list[CollectedJob]:

        response = httpx.get(
            REMOTIVE_API_URL,
            timeout=self.timeout
        )

        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data.get("jobs", []):
            jobs.append(self._normalize_job(job))

        return jobs

    def _normalize_job(self, job: dict) -> CollectedJob:

        salary_min = None
        salary_max = None
        currency = None

        salary = job.get("salary")

        if salary:
            salary_text = salary.lower()

            if "$" in salary_text:
                currency = "USD"

        posted_date = None

        if job.get("publication_date"):
            posted_date = datetime.fromisoformat(
                job["publication_date"].replace("Z", "+00:00")
            )

        return CollectedJob(
            source="remotive",
            external_job_id=str(job.get("id")),

            company=job.get("company_name", "Unknown"),
            title=job.get("title", "Unknown"),

            description=job.get(
                "description",
                ""
            ),

            location=job.get(
                "candidate_required_location"
            ),

            country=None,

            remote_type="remote",

            salary_min=salary_min,
            salary_max=salary_max,
            currency=currency,

            job_url=job.get(
                "url",
                ""
            ),

            posted_date=posted_date
        )