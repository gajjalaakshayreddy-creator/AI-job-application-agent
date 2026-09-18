from fastapi import FastAPI

from src.api.routes.jobs import router as jobs_router
from src.database.database import create_tables


app = FastAPI(
    title="AI Job Application Agent API",
    description="Backend API for job collection, search, and matching.",
    version="1.0.0",
)


@app.on_event("startup")
def startup() -> None:
    create_tables()


app.include_router(jobs_router)


@app.get("/", tags=["Health"])
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "AI Job Application Agent",
    }