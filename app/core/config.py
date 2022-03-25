from typing import List

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    """Defines project global settings"""

    API_STR: str = "/api"
    PROJECT_TITLE: str = "Online Book Store API"
    PROJECT_DESCRIPTION: str = "Backend API for an online Book Store"
    CORS_ORIGINS: List[AnyHttpUrl] = []


settings = Settings()
