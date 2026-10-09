from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from database import engine

app = FastAPI()


class EndpointRequest(BaseModel):
    url: str


@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except OperationalError as exc:
        raise HTTPException(status_code=503, detail="Database unavailable") from exc
    return {"status": "ok", "database": "ok"}


@app.post("/endpoints")
def create_endpoint(endpoint: EndpointRequest):
    return {"url": endpoint.url}
