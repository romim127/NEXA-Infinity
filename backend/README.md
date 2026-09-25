# NEXA Backend

Python/FastAPI services for NEXA Infinity.

## First executable core

The Phase-0 backend establishes the first canonical contract: `NexaEvent`.

Available endpoints:

- `GET /health` — verifies that the NEXA core API is alive.
- `POST /events` — validates a normalized event and returns it.

The event model already carries:

- unique event ID
- UTC timestamp
- event type
- severity
- source
- summary
- optional case ID
- provenance
- extensible attributes

## Run locally

From the `backend` directory:

```bash
python -m venv .venv
```

Activate the virtual environment, install dependencies:

```bash
pip install -r requirements.txt
```

Then start the API:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

## Architectural rule

At this stage `POST /events` deliberately does **not** write evidence or silently mutate case state. It defines and validates the event boundary first. Persistence, correlation and audit storage will be introduced explicitly in later phases.
