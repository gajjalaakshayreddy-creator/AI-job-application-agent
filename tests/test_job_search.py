from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.database import Base
from src.database.models import Job
from src.jobs.service import JobSearchService


def create_test_session(tmp_path):

    database_path = tmp_path / "test.db"

    engine = create_engine(
        f"sqlite:///{database_path}"
    )

    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)

    return SessionLocal()


def create_jobs(session):

    jobs = [
        Job(
            source="test",
            external_job_id="1",
            company="Company A",
            title="Data Engineer",
            description="Build data pipelines.",
            location="Hyderabad",
            country="India",
            remote_type="hybrid",
            job_url="https://example.com/1",
            job_hash="hash-1"
        ),
        Job(
            source="test",
            external_job_id="2",
            company="Company B",
            title="AI Engineer",
            description="Build AI applications.",
            location="Bangalore",
            country="India",
            remote_type="remote",
            job_url="https://example.com/2",
            job_hash="hash-2"
        ),
        Job(
            source="test",
            external_job_id="3",
            company="Company C",
            title="Software Engineer",
            description="Build software applications.",
            location="Chennai",
            country="India",
            remote_type="onsite",
            job_url="https://example.com/3",
            job_hash="hash-3"
        )
    ]

    session.add_all(jobs)
    session.commit()


def test_search_by_role(tmp_path):

    with create_test_session(tmp_path) as session:

        create_jobs(session)

        service = JobSearchService(session)

        jobs = service.search_jobs(
            roles=["Data Engineer"]
        )

        assert len(jobs) == 1
        assert jobs[0].title == "Data Engineer"


def test_search_by_location(tmp_path):

    with create_test_session(tmp_path) as session:

        create_jobs(session)

        service = JobSearchService(session)

        jobs = service.search_jobs(
            locations=["Hyderabad"]
        )

        assert len(jobs) == 1
        assert jobs[0].location == "Hyderabad"


def test_search_by_remote_type(tmp_path):

    with create_test_session(tmp_path) as session:

        create_jobs(session)

        service = JobSearchService(session)

        jobs = service.search_jobs(
            remote_types=["remote"]
        )

        assert len(jobs) == 1
        assert jobs[0].remote_type == "remote"