# relay
Reliable webhook delivery platform with durable retries, worker recovery, and PostgreSQL-backed task claiming.

## Current learning stage

Only `Client -> FastAPI -> PostgreSQL` is implemented. There are no application
tables, database models, delivery workers, or retries yet.

- `main.py`: handles client requests. `GET /health` queries PostgreSQL;
  `POST /endpoints` still only echoes the submitted URL.
- `database.py`: connects FastAPI to PostgreSQL using synchronous SQLAlchemy.
- `compose.yaml`: runs one local PostgreSQL database, with persistent data.
- `requirements.txt`: lists the Python packages needed to run the app.

## Run locally

Use the existing Python 3.12 virtual environment:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
docker compose up -d
```

PostgreSQL initialization may take a few seconds. Check readiness:

```bash
docker compose exec postgres pg_isready -U relay -d relay
```

Then start FastAPI:

```bash
python -m uvicorn main:app --reload
```

In another terminal:

```bash
curl http://127.0.0.1:8000/health
```

The healthy response is `{"status":"ok","database":"ok"}`. Database connection
failures return HTTP 503 with `{"detail":"Database unavailable"}`.

Development-only database credentials are user `relay`, password `relay`, and
database `relay`. PostgreSQL is exposed only on `127.0.0.1:5432`.

Stop FastAPI with Ctrl+C and PostgreSQL with `docker compose down`. The named
Docker volume keeps database data when the container is removed.
