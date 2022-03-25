from fastapi import APIRouter

from . import books, authors

api_router = APIRouter()

api_router.include_router(books.router, prefix="/books", tags=["Books"])
api_router.include_router(authors.router, prefix="/authors", tags=["Authors"])
