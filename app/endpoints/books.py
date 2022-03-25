from fastapi import APIRouter

router = APIRouter()

books = [
    {"id": 1, "title": "book 1", "price": 16.99},
    {"id": 2, "title": "book 2", "price": 12.99},
    {"id": 3, "title": "book 3", "price": 9.99},
]


@router.get("/")
def get_books():
    """Get books from database"""
    return books
