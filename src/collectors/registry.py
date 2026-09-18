from src.collectors.base import JobCollector
from src.collectors.models import CollectedJob


class CollectorRegistry:

    def __init__(self):
        self._collectors: list[JobCollector] = []

    def register(self, collector: JobCollector) -> None:
        self._collectors.append(collector)

    def get_collectors(self) -> list[JobCollector]:
        return self._collectors.copy()

    def collect_all(self) -> list[CollectedJob]:
        collected_jobs: list[CollectedJob] = []

        for collector in self._collectors:
            jobs = collector.fetch_jobs()
            collected_jobs.extend(jobs)

        return collected_jobs