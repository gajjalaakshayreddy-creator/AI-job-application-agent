from abc import ABC, abstractmethod

from .models import CollectedJob


class JobCollector(ABC):

    @abstractmethod
    def fetch_jobs(self) -> list[CollectedJob]:
        """Fetch and normalize jobs from a job source."""
        raise NotImplementedError