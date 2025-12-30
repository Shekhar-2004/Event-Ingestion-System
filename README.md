# Event Ingestion System

A FastAPI-based service for ingesting and processing events in real-time. Week 1 implementation provides a basic skeleton with event ingestion API.

## Features

- **FastAPI Framework**: High-performance async web framework for building APIs
- **Pydantic Models**: Data validation and serialization using Pydantic
- **Event Processing**: Modular architecture for handling different types of events
- **RESTful API**: Clean REST endpoints for event submission
- **Health Checks**: Built-in health check endpoints for monitoring

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Event_Ingestion
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv menv
   # On Windows:
   menv\Scripts\activate
   # On macOS/Linux:
   source menv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The API will be available at `http://localhost:8000`

3. View the interactive API documentation at `http://localhost:8000/docs`

### API Endpoints

- `POST /api/v1/events` - Submit a new event
- `GET /` - Health check endpoint
- `GET /health` - Simple health check

### Example Usage

Submit an event:
```bash
curl -X POST "http://localhost:8000/api/v1/events" \
     -H "Content-Type: application/json" \
     -d '{
       "event_type": "user_action",
       "payload": {
         "action": "login",
         "user_id": "12345"
       }
     }'
```

Response:
```json
{
  "message": "Event accepted for processing",
  "event_id": "generated-uuid",
  "status": "queued"
}
```

## Project Structure

```
Event_Ingestion/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── models.py            # Pydantic data models (Event)
│   ├── routes/
│   │   ├── events.py        # Event-related API routes
│   │   └── __init__.py
│   └── services/
│       ├── processor.py     # Event processing logic (Week 1 stub)
│       └── __init__.py
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md              # This file
```

## Development

- Add new event types in `app/models.py`
- Implement route handlers in `app/routes/events.py`
- Add business logic in `app/services/processor.py`

## Support

For questions and support:
- Open an issue on GitHub
- Check the API documentation at `/docs` when running
- Health check available at `/health`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Please ensure all tests pass and code follows the project's style guidelines.