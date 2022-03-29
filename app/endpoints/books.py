from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

router = APIRouter()

books = [
    {"id": 1, "title": "book 1", "price": 16.99},
    {"id": 2, "title": "book 2", "price": 12.99},
    {"id": 3, "title": "book 3", "price": 9.99},
]


@router.get("/")
def get_books(limit: int = 1, skip: int = 0):
    """Get books from database"""
    response = books[skip : skip + limit]
    return response


@router.post("/")
def add_book(new_book):
    """Create new book and store in database"""
    books.append(new_book)

    return books


@router.get("/{book_id}")
def get_book_by_id(book_id: int):
    """Get single book from database"""
    for book in books:
        if book["id"] == book_id:
            return book


@router.put("/{book_id}")
def update_book(book_id: int, book):
    """Update book in database"""
    update_book_encoded = jsonable_encoder(book)
    books[book_id] = update_book_encoded

    return update_book_encoded


@router.delete("/{book_id}")
def delete_book(book_id: int):
    """Delete book from database"""
    for book in books:
        if book["id"] == book_id:
            books.pop(book_id - 1)

    return books
