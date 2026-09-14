from pathlib import Path
from src.candidate.loader import load_candidate_profile


PROFILE_PATH = Path("data/candidate_profile.json")


def test_candidate_profile_loads():
    profile = load_candidate_profile(PROFILE_PATH)

    assert profile.candidate.personal_information.name == "Gajjala Akshay Reddy"


def test_candidate_has_skills():
    profile = load_candidate_profile(PROFILE_PATH)

    skills = profile.candidate.skills

    assert "Python" in skills.programming
    assert "SQL" in skills.programming
    assert "Microsoft Azure" in skills.cloud


def test_candidate_has_target_roles():
    profile = load_candidate_profile(PROFILE_PATH)

    roles = profile.candidate.preferences.target_roles

    assert len(roles) > 0