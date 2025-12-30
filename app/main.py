from fastapi import FastAPI
import logging
from app.routes import events

# configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# create FastAPI app
app = FastAPI(
    title="Event Ingestion System",
    description="Week 1: Basic skelton with event ingestion API",
    version = "1.0.0"
)

#include routes
app.include_router(events.router, prefix="/api/v1")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status" : "running",
        "message" : "Event investigation system - Week 1 Skelton",
        "endpoints" : {
            "ingest_event" : "POST/api/v1/events",
            "health" : "GET /"
        }
    }
    
@app.get("/health")
async def health_check():
    """Simple Health Check"""
    return { "status": "healthy" }