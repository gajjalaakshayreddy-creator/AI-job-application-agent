from pydantic import BaseModel, Field


class JobRequirements(BaseModel):
    role: str
    seniority: str | None = None

    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)

    minimum_experience_years: float | None = None

    education_requirements: list[str] = Field(default_factory=list)

    responsibilities: list[str] = Field(default_factory=list)