from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from src.api.dependencies import get_db
from src.api.schemas import JobResponse
from src.jobs.service import JobSearchService


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get(
    "/search",
    response_model=list[JobResponse],
)
def search_jobs(
    roles: list[str] | None = Query(default=None),
    locations: list[str] | None = Query(default=None),
    remote_types: list[str] | None = Query(default=None),
    country: str | None = None,
    status: str = "ACTIVE",
    limit: int = Query(
        default=50,
        ge=1,
        le=100,
    ),
    db: Session = Depends(get_db),
) -> list[JobResponse]:

    service = JobSearchService(db)

    jobs = service.search_jobs(
        roles=roles,
        locations=locations,
        remote_types=remote_types,
        country=country,
        status=status,
        limit=limit,
    )

    return jobs