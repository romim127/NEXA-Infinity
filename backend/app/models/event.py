from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class NexaSeverity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class NexaProvenance(BaseModel):
    source_type: str = Field(..., examples=["live_acquisition", "pcap", "rf", "manual"])
    source_name: str
    evidence_id: str | None = None
    collector: str | None = None
    hash_sha256: str | None = None


class NexaEvent(BaseModel):
    event_id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    event_type: str
    severity: NexaSeverity = NexaSeverity.INFO
    source: str
    summary: str
    case_id: str | None = None
    provenance: NexaProvenance
    attributes: dict[str, Any] = Field(default_factory=dict)
