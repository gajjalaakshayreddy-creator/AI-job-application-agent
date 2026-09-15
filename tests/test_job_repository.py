from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.collectors.models import CollectedJob
from src.database.database import Base
from src.database.job_repository import JobRepository


def create_test_session(tmp_path):

    database_path = tmp_path / "test.db"

    engine = create_engine(
        f"sqlite:///{database_path}"
    )

    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)

    return SessionLocal()


def create_sample_job():

    return CollectedJob(
        source="test",
        external_job_id="123",
        company="Test AI",
        title="AI Engineer",
        description="Build AI applications.",
        location="Hyderabad",
        country="India",
        remote_type="remote",
        salary_min=None,
        salary_max=None,
        currency=None,
        job_url="https://example.com/job/123",
        posted_date=None
    )


def test_save_new_job(tmp_path):

    with create_test_session(tmp_path) as session:

        repository = JobRepository(session)

        job, created = repository.save_job(
            create_sample_job()
        )

        assert created is True
        assert job.id is not None
        assert job.company == "Test AI"


def test_duplicate_job_is_not_inserted(tmp_path):

    with create_test_session(tmp_path) as session:

        repository = JobRepository(session)

        job1, created1 = repository.save_job(
            create_sample_job()
        )

        job2, created2 = repository.save_job(
            create_sample_job()
        )

        assert created1 is True
        assert created2 is False
        assert job1.id == job2.id