from src.matching.models import JobMatchResult
from src.matching.scorer import (
    calculate_overall_score,
    get_recommendation,
)
from src.matching.skill_matcher import calculate_skill_match
from src.requirements.models import JobRequirements


class JobMatchingService:

    def match_job(
        self,
        job,
        profile,
        requirements: JobRequirements,
        experience_score: float,
        role_score: float,
        location_score: float,
        work_mode_score: float,
    ) -> JobMatchResult:

        candidate_skills = []

        skills = profile.candidate.skills

        candidate_skills.extend(skills.programming)
        candidate_skills.extend(skills.data)
        candidate_skills.extend(skills.cloud)
        candidate_skills.extend(skills.ai_ml)
        candidate_skills.extend(skills.databases)
        candidate_skills.extend(skills.frameworks)

        skill_result = calculate_skill_match(
            candidate_skills,
            requirements.required_skills,
        )

        skill_score = skill_result["match_percentage"]

        overall_score = calculate_overall_score(
            skill_score=skill_score,
            experience_score=experience_score,
            role_score=role_score,
            location_score=location_score,
            work_mode_score=work_mode_score,
        )

        return JobMatchResult(
            job_id=job.id,
            job_title=job.title,
            company=job.company,
            overall_score=overall_score,
            skill_score=skill_score,
            experience_score=experience_score,
            role_score=role_score,
            location_score=location_score,
            matched_skills=skill_result["matched_skills"],
            missing_skills=skill_result["missing_skills"],
            recommendation=get_recommendation(overall_score),
        )