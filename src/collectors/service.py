from src.database.job_repository import JobRepository

from .base import JobCollector


class JobIngestionService:

    def __init__(
        self,
        collector: JobCollector,
        repository: JobRepository
    ):
        self.collector = collector
        self.repository = repository

    def ingest(self) -> dict:

        jobs = self.collector.fetch_jobs()

        new_jobs = 0
        duplicate_jobs = 0

        for job in jobs:

            _, created = self.repository.save_job(job)

            if created:
                new_jobs += 1
            else:
                duplicate_jobs += 1

        return {
            "fetched": len(jobs),
            "new": new_jobs,
            "duplicates": duplicate_jobs
        }