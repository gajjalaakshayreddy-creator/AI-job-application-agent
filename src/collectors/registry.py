import logging

from src.collectors.base import JobCollector
from src.collectors.models import CollectedJob


logger = logging.getLogger(__name__)


class CollectorRegistry:

    def __init__(self) -> None:
        self._collectors: list[JobCollector] = []

    def register(self, collector: JobCollector) -> None:
        self._collectors.append(collector)

    def get_collectors(self) -> list[JobCollector]:
        return self._collectors.copy()

    def collect_all(self) -> list[CollectedJob]:
        collected_jobs: list[CollectedJob] = []

        for collector in self._collectors:
            collector_name = collector.__class__.__name__

            try:
                logger.info(
                    "Starting collection: %s",
                    collector_name,
                )

                jobs = collector.fetch_jobs()

                collected_jobs.extend(jobs)

                logger.info(
                    "Completed collection: %s | Jobs fetched: %d",
                    collector_name,
                    len(jobs),
                )

            except Exception:
                logger.exception(
                    "Collector failed: %s",
                    collector_name,
                )

                # Continue with the remaining collectors.
                continue

        return collected_jobs