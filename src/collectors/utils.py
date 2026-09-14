import hashlib


def generate_job_hash(
    company: str,
    title: str,
    location: str | None
) -> str:

    raw = "|".join(
        [
            company.strip().lower(),
            title.strip().lower(),
            (location or "").strip().lower()
        ]
    )

    return hashlib.sha256(
        raw.encode("utf-8")
    ).hexdigest()