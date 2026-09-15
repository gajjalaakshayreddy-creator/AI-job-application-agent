from abc import ABC, abstractmethod

from .models import JobRequirements


class RequirementExtractor(ABC):

    @abstractmethod
    def extract(self, job_description: str) -> JobRequirements:
        raise NotImplementedError
class MockRequirementExtractor(RequirementExtractor):

    def extract(self, job_description: str) -> JobRequirements:
        return JobRequirements(
            role="AI Engineer",
            seniority="Mid-Level",
            required_skills=[
                "Python",
                "Azure",
                "RAG"
            ],
            preferred_skills=[
                "LangChain",
                "Docker"
            ],
            minimum_experience_years=2,
            education_requirements=[
                "Bachelor's degree in Computer Science"
            ],
            responsibilities=[
                "Build AI applications",
                "Develop RAG systems"
            ]
        )