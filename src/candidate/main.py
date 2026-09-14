from .loader import load_candidate_profile


def main():
    profile = load_candidate_profile(
        "data/candidate_profile.json"
    )

    candidate = profile.candidate

    print(f"Name: {candidate.personal_information.name}")
    print(f"Current Role: {candidate.professional_information.current_role}")
    print(
        f"Experience: "
        f"{candidate.professional_information.years_of_experience} years"
    )

    print("\nTarget Roles:")
    for role in candidate.preferences.target_roles:
        print(f"- {role}")

    print("\nAI/ML Skills:")
    for skill in candidate.skills.ai_ml:
        print(f"- {skill}")


if __name__ == "__main__":
    main()