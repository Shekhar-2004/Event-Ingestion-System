from fastapi import APIRouter, HTTPException
import logging
from app.models import Event
from app.services.processor import process_event

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/events", status_code=202)
async def ingest_event(event:Event):
    """
    Week 1 Event Ingestion Endpoint
    
    What it does:
    1. Accepts an event
    2. Validates input (automatic via Pydantic)
    3. Logs receipt
    4. Hands off to processor
    5. Returns immediately (202 Accepted)
    
    This is the API contract for Week 1.
    """
    try:
        logger.info(f"Event received: {event.id} (type: {event.event_type})")
        process_event(event)
        
        return {
            "message": "Event accepted for processing",
            "event_id": event.id,
            "status" : "queued"
        }
        
    except Exception as e:
        logger.error(f"Erorr processing event {event.id}: {str(e)}")
        raise HTTPException(
            status_code= 400,
            detail=f"Failed to process event: {str(e)}"
        )