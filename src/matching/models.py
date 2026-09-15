from pydantic import BaseModel


class SkillMatchResult(BaseModel):
    matched_skills: list[str]
    missing_skills: list[str]
    match_percentage: float


class JobMatchResult(BaseModel):
    job_id: int
    job_title: str
    company: str

    overall_score: float

    skill_score: float
    experience_score: float
    role_score: float
    location_score: float

    matched_skills: list[str]
    missing_skills: list[str]

    recommendation: str