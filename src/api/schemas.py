from datetime import datetime

from pydantic import BaseModel, ConfigDict


class JobResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
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
    discovered_date: datetime
    status: str