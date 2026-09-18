from src.collectors.models import CollectedJob
from src.collectors.registry import CollectorRegistry


class FakeCollector:

    def __init__(self, jobs):
        self.jobs = jobs

    def fetch_jobs(self):
        return self.jobs


def create_job(title: str) -> CollectedJob:

    return CollectedJob(
        source="test",
        external_job_id=title,
        company="Test Company",
        title=title,
        description="Test job description",
        location="Remote",
        country=None,
        remote_type="remote",
        salary_min=None,
        salary_max=None,
        currency=None,
        job_url="https://example.com/job",
        posted_date=None,
    )


def test_registry_collects_from_multiple_sources():

    registry = CollectorRegistry()

    collector_a = FakeCollector(
        [create_job("Python Developer")]
    )

    collector_b = FakeCollector(
        [create_job("Data Engineer")]
    )

    registry.register(collector_a)
    registry.register(collector_b)

    jobs = registry.collect_all()

    assert len(jobs) == 2
    assert jobs[0].title == "Python Developer"
    assert jobs[1].title == "Data Engineer"


def test_registry_starts_empty():

    registry = CollectorRegistry()

    assert registry.get_collectors() == []
    assert registry.collect_all() == []