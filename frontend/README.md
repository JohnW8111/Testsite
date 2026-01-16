# Frontend

Simple static HTML dashboard to display the Consumer Discretionary growth score.

## Run
Open `frontend/index.html` in a browser, or serve it with a static server:
```bash
python -m http.server 8080
```

## Configuration
By default, it calls:
- `http://localhost:8000/api/growth/consumer-discretionary`

If you need a different backend URL, set `window.API_BASE` before the script runs.
