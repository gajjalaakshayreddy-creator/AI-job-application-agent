SKILL_ALIASES = {
    "python 3": "python",
    "python": "python",

    "microsoft azure": "azure",
    "azure cloud": "azure",
    "azure": "azure",

    "microsoft fabric": "microsoft fabric",
    "ms fabric": "microsoft fabric",

    "postgres": "postgresql",
    "postgresql": "postgresql",

    "llm": "llm",
    "large language model": "llm",
    "large language models": "llm",

    "rag": "rag",
    "retrieval augmented generation": "rag",

    "ai agents": "ai agents",
    "ai agent": "ai agents",
    "agents": "ai agents",

    "pyspark": "pyspark",
    "spark": "spark"
}


def normalize_skill(skill: str) -> str:
    skill = skill.strip().lower()

    return SKILL_ALIASES.get(
        skill,
        skill
    )


def normalize_skills(skills: list[str]) -> set[str]:

    return {
        normalize_skill(skill)
        for skill in skills
    }


def calculate_skill_match(
    candidate_skills: list[str],
    required_skills: list[str]
):

    candidate = normalize_skills(
        candidate_skills
    )

    required = normalize_skills(
        required_skills
    )

    if not required:
        return {
            "matched_skills": [],
            "missing_skills": [],
            "match_percentage": 0.0
        }

    matched = candidate.intersection(required)

    missing = required - candidate

    percentage = (
        len(matched) / len(required)
    ) * 100

    return {
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "match_percentage": round(
            percentage,
            2
        )
    }