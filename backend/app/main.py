from datetime import datetime, timezone

from fastapi import FastAPI

from app.models.event import NexaEvent


app = FastAPI(
    title="NEXA Infinity API",
    version="0.1.0-dev",
    description="Core API for the NEXA Infinity forensic and defensive analysis platform.",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "nexa-infinity-core",
        "version": app.version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/events", response_model=NexaEvent, tags=["events"])
def ingest_event(event: NexaEvent) -> NexaEvent:
    """
    Phase-0 ingestion contract.

    This endpoint currently validates and returns a normalized NEXA event.
    Persistence, correlation and audit storage will be added in later phases.
    """
    return event
