from pydantic import BaseModel, HttpUrl
from typing import List


class PersonalInformation(BaseModel):
    name: str
    email: str
    phone: str
    location: str
    linkedin: HttpUrl
    github: HttpUrl


class ProfessionalInformation(BaseModel):
    current_role: str
    years_of_experience: float
    previous_roles: List[str]
    companies: List[str]
    projects: List[str]


class Skills(BaseModel):
    programming: List[str]
    data: List[str]
    cloud: List[str]
    ai_ml: List[str]
    databases: List[str]
    frameworks: List[str]


class Education(BaseModel):
    degree: str
    university: str
    graduation_year: int


class SalaryPreference(BaseModel):
    amount: float
    currency: str
    unit: str


class Preferences(BaseModel):
    target_roles: List[str]
    locations: List[str]
    work_mode: List[str]
    minimum_salary: SalaryPreference
    visa_sponsorship: bool


class Candidate(BaseModel):
    personal_information: PersonalInformation
    professional_information: ProfessionalInformation
    skills: Skills
    education: List[Education]
    preferences: Preferences


class CandidateProfile(BaseModel):
    candidate: Candidate