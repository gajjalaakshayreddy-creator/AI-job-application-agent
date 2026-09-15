from sqlalchemy.orm import Session

from src.collectors.models import CollectedJob
from src.collectors.utils import generate_job_hash
from src.database.models import Job


class JobRepository:

    def __init__(self, session: Session):
        self.session = session

    def save_job(self, collected_job: CollectedJob) -> tuple[Job, bool]:
        job_hash = generate_job_hash(
            collected_job.company,
            collected_job.title,
            collected_job.location
        )

        existing_job = (
            self.session.query(Job)
            .filter(Job.job_hash == job_hash)
            .first()
        )

        if existing_job:
            return existing_job, False

        job = Job(
            source=collected_job.source,
            external_job_id=collected_job.external_job_id,
            company=collected_job.company,
            title=collected_job.title,
            description=collected_job.description,
            location=collected_job.location,
            country=collected_job.country,
            remote_type=collected_job.remote_type,
            salary_min=collected_job.salary_min,
            salary_max=collected_job.salary_max,
            currency=collected_job.currency,
            job_url=collected_job.job_url,
            posted_date=collected_job.posted_date,
            job_hash=job_hash
        )

        self.session.add(job)
        self.session.commit()
        self.session.refresh(job)

        return job, True