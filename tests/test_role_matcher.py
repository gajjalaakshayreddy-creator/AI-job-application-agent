from src.matching.role_matcher import calculate_role_score


def test_exact_role_match():
    score = calculate_role_score(
        ["AI Engineer", "Software Engineer"],
        "AI Engineer",
    )

    assert score == 100


def test_partial_role_match():
    score = calculate_role_score(
        ["Software Engineer"],
        "Senior Software Engineer",
    )

    assert score == 80


def test_different_role():
    score = calculate_role_score(
        ["Software Engineer"],
        "Data Scientist",
    )

    assert score == 40


def test_missing_job_role():
    score = calculate_role_score(
        ["Software Engineer"],
        None,
    )

    assert score == 100