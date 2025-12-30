import logging

logger = logging.getLogger(__name__)

def process_event(event):
    """
    Stub function that will process events in the future.
    
    For Week 1, we just log that we received the event.
    This demonstrates the "hand-off" concept.
    
    In future weeks, this will:
    1. Store events in a database
    2. Trigger business logic
    3. Send to message queues
    4. etc.
    """
    logger.info(f"Processing event in background: {event.id}")
    
    # Week 1: Just log the hand-off
    # Week 2+: Actual processing logic will go here
    return {"status": "queued_for_processing", "event_id": event.id}