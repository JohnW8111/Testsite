# Backend API

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
export FRED_API_KEY="your_key"
uvicorn app:app --reload --port 8000
```

## Endpoint
- `GET /api/growth/consumer-discretionary`
  - Returns a weighted growth score and signal breakdown using public FRED data.

## Environment variables
- `FRED_API_KEY` (required)
- `ALLOWED_ORIGINS` (optional, comma-separated; defaults to `*`)
