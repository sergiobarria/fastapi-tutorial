from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints.api import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, description=settings.PROJECT_DESCRIPTION)

app.include_router(api_router, prefix=settings.API_STR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    """Entry path for the application"""
    return {"message": "Hello World"}
