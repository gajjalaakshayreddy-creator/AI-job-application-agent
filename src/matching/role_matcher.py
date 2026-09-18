def calculate_role_score(
    candidate_roles: list[str],
    job_role: str | None,
) -> float:

    if not job_role:
        return 100.0

    job_role_normalized = job_role.lower().strip()

    for role in candidate_roles:
        role_normalized = role.lower().strip()

        if role_normalized == job_role_normalized:
            return 100.0

        if (
            role_normalized in job_role_normalized
            or job_role_normalized in role_normalized
        ):
            return 80.0

    return 40.0