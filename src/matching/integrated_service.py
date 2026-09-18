from src.matching.experience import calculate_experience_score
from src.matching.role_matcher import calculate_role_score
from src.matching.service import JobMatchingService


class IntegratedJobMatchingService:

    def __init__(self):
        self.matcher = JobMatchingService()

    def match(
        self,
        job,
        profile,
        requirements,
    ):

        candidate_years = (
            profile.candidate
            .professional_information
            .years_of_experience
        )

        experience_score = calculate_experience_score(
            candidate_years,
            requirements.minimum_experience_years,
        )

        candidate_roles = (
            profile.candidate
            .preferences
            .target_roles
        )

        role_score = calculate_role_score(
            candidate_roles,
            requirements.role,
        )

        # Step 9 keeps these deterministic for now.
        location_score = 100.0
        work_mode_score = 100.0

        return self.matcher.match_job(
            job=job,
            profile=profile,
            requirements=requirements,
            experience_score=experience_score,
            role_score=role_score,
            location_score=location_score,
            work_mode_score=work_mode_score,
        )