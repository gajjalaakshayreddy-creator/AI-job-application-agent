from src.matching.integrated_service import IntegratedJobMatchingService
from src.requirements.extractor import MockRequirementExtractor
from src.requirements.service import JobRequirementService


def test_integrated_job_matching(sample_job, candidate_profile):
    extractor = MockRequirementExtractor()

    requirement_service = JobRequirementService(
        extractor
    )

    requirements = requirement_service.extract_requirements(
        sample_job.description
    )

    matching_service = IntegratedJobMatchingService()

    result = matching_service.match(
        job=sample_job,
        profile=candidate_profile,
        requirements=requirements,
    )

    assert result.job_id == sample_job.id
    assert result.overall_score >= 0
    assert result.overall_score <= 100

    assert result.skill_score >= 0
    assert result.skill_score <= 100

    assert isinstance(result.matched_skills, list)
    assert isinstance(result.missing_skills, list)