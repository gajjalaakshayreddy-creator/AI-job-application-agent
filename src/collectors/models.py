from datetime import datetime

from pydantic import BaseModel


class CollectedJob(BaseModel):
    source: str
    external_job_id: str | None

    company: str
    title: str
    description: str

    location: str | None
    country: str | None
    remote_type: str | None

    salary_min: float | None
    salary_max: float | None
    currency: str | None

    job_url: str

    posted_date: datetime | None