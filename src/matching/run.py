from src.candidate.loader import load_candidate_profile
from src.database.database import SessionLocal
from src.database.models import Job
from src.matching.service import JobMatchingService


PROFILE_PATH = "data/candidate_profile.json"


def main():

    profile = load_candidate_profile(
        PROFILE_PATH
    )

    with SessionLocal() as session:

        job = (
            session.query(Job)
            .first()
        )

        if not job:
            print("No jobs found in database.")
            return

        required_skills = [
            "Python",
            "SQL",
            "Azure",
            "LLM",
            "RAG"
        ]

        service = JobMatchingService()

        result = service.match_job(
            job=job,
            profile=profile,
            required_skills=required_skills,
            experience_score=80,
            role_score=90,
            location_score=100,
            work_mode_score=100
        )

        print("\nJOB MATCH")
        print("=========")

        print(f"Job: {result.job_title}")
        print(f"Company: {result.company}")
        print(f"Overall Score: {result.overall_score}")
        print(f"Skill Score: {result.skill_score}")

        print("\nMatched Skills:")

        for skill in result.matched_skills:
            print(f"  ✓ {skill}")

        print("\nMissing Skills:")

        for skill in result.missing_skills:
            print(f"  ✗ {skill}")

        print(
            f"\nRecommendation: "
            f"{result.recommendation}"
        )


if __name__ == "__main__":
    main()