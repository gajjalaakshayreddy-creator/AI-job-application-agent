import pytest
from src.database.models import Job
from src.candidate.models import (
    CandidateProfile,
    Candidate,
    PersonalInformation,
    ProfessionalInformation,
    Skills,
    Education,
    Preferences,
    SalaryPreference,
)


@pytest.fixture
def sample_job():
    return Job(
        id=1,
        source="test",
        external_job_id="test-001",
        company="Test Company",
        title="Python Data Engineer",
        description=(
            "We are looking for a Python Data Engineer with experience in "
            "Python, SQL, PySpark, Azure, and ETL pipelines."
        ),
        location="Hyderabad",
        country="India",
        remote_type="HYBRID",
        salary_min=800000,
        salary_max=1200000,
        currency="INR",
        job_url="https://example.com/jobs/test-001",
        job_hash="test-job-hash-001",
        status="ACTIVE",
    )


@pytest.fixture
def candidate_profile():
    return CandidateProfile(
        candidate=Candidate(
            personal_information=PersonalInformation(
                name="Test Candidate",
                email="test@example.com",
                phone="9999999999",
                location="Hyderabad",
                linkedin="https://www.linkedin.com/in/test-candidate",
                github="https://github.com/test-candidate",
            ),
            professional_information=ProfessionalInformation(
                current_role="Software Engineer I",
                years_of_experience=2.0,
                previous_roles=["Software Engineer"],
                companies=["MAQ Software"],
                projects=[
                    "Fabric Platform Modernization",
                    "Lender Data Sharing Platform",
                ],
            ),
            skills=Skills(
                programming=["Python", "C#", "SQL", "C++"],
                data=[
                    "Microsoft Fabric",
                    "PySpark",
                    "ETL Pipelines",
                    "Data Migration",
                ],
                cloud=["Azure"],
                ai_ml=["LLMs", "RAG", "LangChain"],
                databases=["SQL Server", "Snowflake", "MySQL"],
                frameworks=[".NET", "React", "Angular", "LangChain"],
            ),
            education=[
                Education(
                    degree="B.Tech in Computer Science and Engineering",
                    university="IIIT Kottayam",
                    graduation_year=2025,
                )
            ],
            preferences=Preferences(
                target_roles=[
                    "Data Engineer",
                    "Software Engineer",
                    "AI Engineer",
                ],
                locations=["Hyderabad", "Remote"],
                work_mode=["HYBRID", "REMOTE"],
                minimum_salary=SalaryPreference(
                    amount=900000,
                    currency="INR",
                    unit="annual",
                ),
                visa_sponsorship=False,
            ),
        )
    )
