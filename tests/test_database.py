from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.database import Base
from src.database.models import Job


def test_job_table_creation(tmp_path: Path):
    database_path = tmp_path / "test.db"

    engine = create_engine(
        f"sqlite:///{database_path}"
    )

    Base.metadata.create_all(bind=engine)

    assert "jobs" in Base.metadata.tables


def test_create_job(tmp_path: Path):
    database_path = tmp_path / "test.db"

    engine = create_engine(
        f"sqlite:///{database_path}"
    )

    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)

    with SessionLocal() as session:
        job = Job(
            source="test",
            external_job_id="TEST-001",
            company="Test Company",
            title="AI Engineer",
            description="Build AI applications using Python and LLMs.",
            location="Hyderabad",
            country="India",
            remote_type="Hybrid",
            salary_min=1200000,
            salary_max=1800000,
            currency="INR",
            job_url="https://example.com/jobs/TEST-001",
            job_hash="test-job-hash-001"
        )

        session.add(job)
        session.commit()

        assert job.id is not None
        assert job.company == "Test Company"
        assert job.title == "AI Engineer"