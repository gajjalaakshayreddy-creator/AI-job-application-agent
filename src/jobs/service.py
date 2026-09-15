from sqlalchemy.orm import Session

from src.database.models import Job


class JobSearchService:

    def __init__(self, session: Session):
        self.session = session

    def search_jobs(
        self,
        roles: list[str] | None = None,
        locations: list[str] | None = None,
        remote_types: list[str] | None = None,
        country: str | None = None,
        status: str = "ACTIVE",
        limit: int = 50
    ) -> list[Job]:

        query = self.session.query(Job)

        # Filter by status
        if status:
            query = query.filter(
                Job.status == status
            )

        # Filter by job roles
        if roles:
            role_filters = [
                Job.title.ilike(f"%{role}%")
                for role in roles
            ]

            from sqlalchemy import or_

            query = query.filter(
                or_(*role_filters)
            )

        # Filter by locations
        if locations:
            location_filters = [
                Job.location.ilike(f"%{location}%")
                for location in locations
            ]

            from sqlalchemy import or_

            query = query.filter(
                or_(*location_filters)
            )

        # Filter by remote type
        if remote_types:
            remote_filters = [
                Job.remote_type.ilike(f"%{remote_type}%")
                for remote_type in remote_types
            ]

            from sqlalchemy import or_

            query = query.filter(
                or_(*remote_filters)
            )

        # Filter by country
        if country:
            query = query.filter(
                Job.country.ilike(f"%{country}%")
            )

        return (
            query
            .order_by(Job.posted_date.desc())
            .limit(limit)
            .all()
        )