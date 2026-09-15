from .extractor import RequirementExtractor
from .models import JobRequirements


class JobRequirementService:

    def __init__(self, extractor: RequirementExtractor):
        self.extractor = extractor

    def extract_requirements(
        self,
        job_description: str
    ) -> JobRequirements:

        if not job_description.strip():
            raise ValueError("Job description cannot be empty")

        return self.extractor.extract(job_description)