from src.collectors.models import CollectedJob
from src.collectors.multi_source_service import (
    MultiSourceIngestionService,
)
from src.collectors.registry import CollectorRegistry


class FakeCollector:

    def __init__(self, jobs):
        self.jobs = jobs

    def fetch_jobs(self):
        return self.jobs


class FakeRepository:

    def __init__(self):
        self.saved_jobs = []

    def save_job(self, collected_job):

        is_duplicate = any(
            job.title == collected_job.title
            for job in self.saved_jobs
        )

        if is_duplicate:
            return collected_job, False

        self.saved_jobs.append(collected_job)

        return collected_job, True


def create_job(title: str) -> CollectedJob:

    return CollectedJob(
        source="test",
        external_job_id=title,
        company="Test Company",
        title=title,
        description="Test description",
        location="Remote",
        country=None,
        remote_type="remote",
        salary_min=None,
        salary_max=None,
        currency=None,
        job_url="https://example.com/job",
        posted_date=None,
    )


def test_multi_source_ingestion():

    registry = CollectorRegistry()

    registry.register(
        FakeCollector([
            create_job("Python Developer"),
            create_job("Data Engineer"),
        ])
    )

    registry.register(
        FakeCollector([
            create_job("Python Developer"),
        ])
    )

    repository = FakeRepository()

    service = MultiSourceIngestionService(
        registry=registry,
        repository=repository,
    )

    summary = service.ingest()

    assert summary["fetched"] == 3
    assert summary["new"] == 2
    assert summary["duplicates"] == 1