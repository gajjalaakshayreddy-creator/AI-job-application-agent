def calculate_experience_score(
    candidate_years: float,
    required_years: float | None,
) -> float:

    if required_years is None:
        return 100.0

    if required_years <= 0:
        return 100.0

    if candidate_years >= required_years:
        return 100.0

    score = (candidate_years / required_years) * 100

    return round(score, 2)