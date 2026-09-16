from src.matching.models import JobMatchResult


class JobRankingService:

    def rank_jobs(
        self,
        match_results: list[JobMatchResult],
        limit: int = 10,
    ) -> list[JobMatchResult]:

        if limit <= 0:
            raise ValueError("Limit must be greater than zero")

        ranked_jobs = sorted(
            match_results,
            key=lambda result: result.overall_score,
            reverse=True,
        )

        return ranked_jobs[:limit]

    def filter_recommendations(
        self,
        match_results: list[JobMatchResult],
        minimum_score: float = 70.0,
    ) -> list[JobMatchResult]:

        if not 0 <= minimum_score <= 100:
            raise ValueError(
                "Minimum score must be between 0 and 100"
            )

        return [
            result
            for result in match_results
            if result.overall_score >= minimum_score
        ]