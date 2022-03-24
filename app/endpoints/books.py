from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_books():
    """Get books from database"""
    return {"data": "books"}


@router.post("/")
def add_book():
    """Create new book and store in database"""
    return {"data": "new book"}


@router.get("/{book_id}")
def get_book_by_id(book_id):
    """Get single book from database"""
    return {"data": "book"}


@router.put("/{book_id}")
def update_book(book_id):
    """Update book in database"""
    return {"data": "updated book"}


@router.delete("/{book_id}")
def delete_book(book_id):
    """Delete book from database"""
    return {}
