from src.matching.skill_matcher import (
    calculate_skill_match,
    normalize_skill
)


def test_skill_normalization():

    assert normalize_skill("Python") == "python"
    assert normalize_skill("Python 3") == "python"
    assert normalize_skill("Microsoft Azure") == "azure"
    assert normalize_skill("RAG") == "rag"


def test_skill_match():

    candidate_skills = [
        "Python",
        "SQL",
        "Azure",
        "RAG"
    ]

    required_skills = [
        "Python",
        "Azure",
        "RAG",
        "Kubernetes"
    ]

    result = calculate_skill_match(
        candidate_skills,
        required_skills
    )

    assert result["match_percentage"] == 75

    assert "python" in result["matched_skills"]
    assert "azure" in result["matched_skills"]
    assert "rag" in result["matched_skills"]

    assert "kubernetes" in result["missing_skills"]