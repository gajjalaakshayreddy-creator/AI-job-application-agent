import logging

from src.collectors.registry import CollectorRegistry
from src.database.job_repository import JobRepository


logger = logging.getLogger(__name__)


class MultiSourceIngestionService:

    def __init__(
        self,
        registry: CollectorRegistry,
        repository: JobRepository,
    ) -> None:
        self.registry = registry
        self.repository = repository

    def ingest(self) -> dict[str, int]:

        logger.info("Starting multi-source ingestion")

        jobs = self.registry.collect_all()

        fetched = len(jobs)
        new_jobs = 0
        duplicates = 0
        failed_saves = 0

        for collected_job in jobs:
            try:
                _, created = self.repository.save_job(
                    collected_job
                )

                if created:
                    new_jobs += 1
                else:
                    duplicates += 1

            except Exception:
                failed_saves += 1

                logger.exception(
                    "Failed to save job: %s - %s",
                    collected_job.company,
                    collected_job.title,
                )

        summary = {
            "fetched": fetched,
            "new": new_jobs,
            "duplicates": duplicates,
            "failed_saves": failed_saves,
        }

        logger.info(
            "Multi-source ingestion completed: %s",
            summary,
        )

        return summary