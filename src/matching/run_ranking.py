from src.matching.ranking import JobRankingService


def display_ranked_jobs(match_results):

    ranking_service = JobRankingService()

    ranked_jobs = ranking_service.rank_jobs(
        match_results,
        limit=10,
    )

    print("\nTop Recommended Jobs")
    print("=" * 60)

    for index, result in enumerate(ranked_jobs, start=1):
        print(
            f"{index}. {result.job_title} | "
            f"{result.company} | "
            f"Score: {result.overall_score} | "
            f"{result.recommendation}"
        )

    return ranked_jobs