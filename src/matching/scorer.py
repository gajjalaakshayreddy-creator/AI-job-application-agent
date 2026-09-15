def calculate_overall_score(
    skill_score: float,
    experience_score: float,
    role_score: float,
    location_score: float,
    work_mode_score: float
) -> float:

    score = (
        skill_score * 0.40
        + experience_score * 0.30
        + role_score * 0.15
        + location_score * 0.10
        + work_mode_score * 0.05
    )

    return round(score, 2)


def get_recommendation(score: float) -> str:

    if score >= 85:
        return "HIGH_PRIORITY"

    if score >= 70:
        return "GOOD_MATCH"

    if score >= 55:
        return "POSSIBLE_MATCH"

    return "LOW_MATCH"