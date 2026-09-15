from sqlalchemy.orm import Session

from src.candidate.models import CandidateProfile
from src.jobs.service import JobSearchService


def search_jobs_for_candidate(
    session: Session,
    profile: CandidateProfile
):

    preferences = profile.candidate.preferences

    service = JobSearchService(session)

    return service.search_jobs(
        roles=preferences.target_roles,
        locations=preferences.locations,
        remote_types=preferences.work_mode
    )