import pytest

from src.requirements.extractor import MockRequirementExtractor
from src.requirements.service import JobRequirementService


def test_requirement_extraction():
    extractor = MockRequirementExtractor()

    service = JobRequirementService(extractor)

    description = """
    We are looking for an AI Engineer with 2+ years of experience.
    Python, Azure and RAG are required.
    LangChain and Docker are preferred.
    """

    result = service.extract_requirements(description)

    assert result.role == "AI Engineer"
    assert result.seniority == "Mid-Level"

    assert "Python" in result.required_skills
    assert "Azure" in result.required_skills
    assert "RAG" in result.required_skills

    assert "LangChain" in result.preferred_skills
    assert "Docker" in result.preferred_skills

    assert result.minimum_experience_years == 2


def test_empty_job_description():
    extractor = MockRequirementExtractor()

    service = JobRequirementService(extractor)

    with pytest.raises(ValueError):
        service.extract_requirements("")