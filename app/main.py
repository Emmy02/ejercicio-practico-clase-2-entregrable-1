import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.database import Base, engine
from app.routers import todos, authors

from app.models import author 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TODO App")
app.include_router(todos.router)
app.include_router(authors.router)

@app.get("/")
def root():
    return {"message": "TODO API is running"}

# --- Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@app.exception_handler(404)
def author_not_found(request: Request, exc: HTTPException):
    logger.warning(f"Ruta no encontrada: {request.method} {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"Ruta no encontrada": exc.detail},
    )