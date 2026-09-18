from src.collectors.greenhouse import GreenhouseCollector
from src.collectors.registry import CollectorRegistry
from src.collectors.remotive import RemotiveCollector
from src.collectors.multi_source_service import (
    MultiSourceIngestionService,
)

from src.database.database import (
    SessionLocal,
    create_tables,
)

from src.database.job_repository import JobRepository

from src.collectors.company_boards import (
    GREENHOUSE_COMPANIES,
)


def main():

    create_tables()

    registry = CollectorRegistry()

    # Remotive
    registry.register(
        RemotiveCollector()
    )

    # Greenhouse companies
    for company_name, board_token in GREENHOUSE_COMPANIES.items():

        print(
            f"Registering Greenhouse collector: {company_name}"
        )

        registry.register(
            GreenhouseCollector(board_token)
        )

    session = SessionLocal()

    try:

        repository = JobRepository(session)

        ingestion_service = MultiSourceIngestionService(
            registry=registry,
            repository=repository,
        )

        summary = ingestion_service.ingest()

        print("\nMulti-Source Ingestion Summary")
        print("=" * 40)

        for key, value in summary.items():
            print(f"{key}: {value}")

    finally:
        session.close()


if __name__ == "__main__":
    main()