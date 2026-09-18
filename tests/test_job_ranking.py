import pytest

from src.matching.models import JobMatchResult
from src.matching.ranking import JobRankingService


def create_match_result(
    job_id: int,
    score: float,
) -> JobMatchResult:

    return JobMatchResult(
        job_id=job_id,
        job_title=f"Job {job_id}",
        company=f"Company {job_id}",
        overall_score=score,
        skill_score=score,
        experience_score=score,
        role_score=score,
        location_score=score,
        matched_skills=[],
        missing_skills=[],
        recommendation="GOOD_MATCH",
    )


def test_jobs_are_ranked_by_score():

    results = [
        create_match_result(1, 60),
        create_match_result(2, 95),
        create_match_result(3, 80),
    ]

    service = JobRankingService()

    ranked = service.rank_jobs(results)

    assert [result.job_id for result in ranked] == [2, 3, 1]


def test_ranking_limit():

    results = [
        create_match_result(1, 60),
        create_match_result(2, 95),
        create_match_result(3, 80),
    ]

    service = JobRankingService()

    ranked = service.rank_jobs(results, limit=2)

    assert len(ranked) == 2
    assert ranked[0].job_id == 2


def test_filter_recommendations():

    results = [
        create_match_result(1, 60),
        create_match_result(2, 95),
        create_match_result(3, 80),
    ]

    service = JobRankingService()

    recommended = service.filter_recommendations(
        results,
        minimum_score=70,
    )

    assert len(recommended) == 2
    assert all(
        result.overall_score >= 70
        for result in recommended
    )


def test_invalid_limit():

    service = JobRankingService()

    with pytest.raises(ValueError):
        service.rank_jobs([], limit=0)