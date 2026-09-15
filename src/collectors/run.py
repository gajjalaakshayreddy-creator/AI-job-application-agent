from src.collectors.remotive import RemotiveCollector
from src.collectors.service import JobIngestionService
from src.database.database import Base, SessionLocal, engine
from src.database.job_repository import JobRepository


def main():

    Base.metadata.create_all(bind=engine)

    collector = RemotiveCollector()

    with SessionLocal() as session:

        repository = JobRepository(session)

        service = JobIngestionService(
            collector=collector,
            repository=repository
        )

        result = service.ingest()

    print("\nJob ingestion completed")
    print("-----------------------")
    print(f"Jobs fetched:   {result['fetched']}")
    print(f"New jobs:       {result['new']}")
    print(f"Duplicates:     {result['duplicates']}")


if __name__ == "__main__":
    main()