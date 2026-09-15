from src.candidate.loader import load_candidate_profile
from src.database.database import SessionLocal
from src.jobs.candidate_search import search_jobs_for_candidate


PROFILE_PATH = "data/candidate_profile.json"


def main():

    profile = load_candidate_profile(
        PROFILE_PATH
    )

    with SessionLocal() as session:

        jobs = search_jobs_for_candidate(
            session,
            profile
        )

    print("\nMatching Jobs")
    print("=============")

    for job in jobs:

        print(
            f"\n{job.title}"
            f"\nCompany: {job.company}"
            f"\nLocation: {job.location}"
            f"\nRemote: {job.remote_type}"
            f"\nURL: {job.job_url}"
        )


if __name__ == "__main__":
    main()