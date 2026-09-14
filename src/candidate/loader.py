import json
from pathlib import Path

from .models import CandidateProfile


def load_candidate_profile(file_path: str | Path) -> CandidateProfile:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Candidate profile not found: {path}"
        )

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return CandidateProfile.model_validate(data)