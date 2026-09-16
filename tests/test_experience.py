from src.matching.experience import calculate_experience_score


def test_candidate_meets_requirement():
    score = calculate_experience_score(2, 2)

    assert score == 100


def test_candidate_exceeds_requirement():
    score = calculate_experience_score(4, 2)

    assert score == 100


def test_candidate_has_less_experience():
    score = calculate_experience_score(1, 2)

    assert score == 50


def test_no_experience_requirement():
    score = calculate_experience_score(1, None)

    assert score == 100