from src.collectors.registry import CollectorRegistry
from src.database.job_repository import JobRepository


class MultiSourceIngestionService:

    def __init__(
        self,
        registry: CollectorRegistry,
        repository: JobRepository,
    ):
        self.registry = registry
        self.repository = repository

    def ingest(self) -> dict[str, int]:

        jobs = self.registry.collect_all()

        fetched = len(jobs)
        new_jobs = 0
        duplicates = 0

        for collected_job in jobs:
            _, created = self.repository.save_job(
                collected_job
            )

            if created:
                new_jobs += 1
            else:
                duplicates += 1

        return {
            "fetched": fetched,
            "new": new_jobs,
            "duplicates": duplicates,
        }