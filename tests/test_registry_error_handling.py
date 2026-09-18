from src.collectors.models import CollectedJob
from src.collectors.registry import CollectorRegistry


class SuccessfulCollector:

    def fetch_jobs(self) -> list[CollectedJob]:
        return [
            CollectedJob(
                source="test",
                external_job_id="1",
                company="Test Company",
                title="Python Developer",
                description="Python development role",
                location="Remote",
                country="India",
                remote_type="Remote",
                salary_min=None,
                salary_max=None,
                currency=None,
                job_url="https://example.com/job/1",
                posted_date=None,
            )
        ]


class FailingCollector:

    def fetch_jobs(self) -> list[CollectedJob]:
        raise RuntimeError("Simulated API failure")


def test_registry_continues_after_collector_failure():

    registry = CollectorRegistry()

    registry.register(FailingCollector())
    registry.register(SuccessfulCollector())

    jobs = registry.collect_all()

    assert len(jobs) == 1
    assert jobs[0].title == "Python Developer"