from src.matching.scorer import (
    calculate_overall_score,
    get_recommendation
)


def test_overall_score():

    score = calculate_overall_score(
        skill_score=90,
        experience_score=80,
        role_score=100,
        location_score=100,
        work_mode_score=100
    )

    assert score == 90


def test_high_priority():

    assert get_recommendation(90) == "HIGH_PRIORITY"


def test_good_match():

    assert get_recommendation(75) == "GOOD_MATCH"


def test_possible_match():

    assert get_recommendation(60) == "POSSIBLE_MATCH"


def test_low_match():

    assert get_recommendation(40) == "LOW_MATCH"