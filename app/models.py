from pydantic import BaseModel, Field
from typing import Dict, Any
from datetime import datetime
import uuid

class Event(BaseModel):
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Unique Event Identifier"
    )
    event_type: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Type of event(e.g., user_action, system_metric)"
    )
    payload : Dict[str, Any] = Field(
        default_factory=dict,
        description="Event data payload"
    )
    timestamp:datetime = Field(
        default_factory=datetime.now,
        description="When the event occured"
    )
    
class Config:
    json_encoders = {
        datetime: lambda dt: dt.isoformat()
    }