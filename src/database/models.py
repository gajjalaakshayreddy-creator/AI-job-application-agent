from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    external_job_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    company: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    country: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    remote_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    salary_min: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    salary_max: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    currency: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    job_url: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )

    posted_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    discovered_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    job_hash: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="ACTIVE",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )