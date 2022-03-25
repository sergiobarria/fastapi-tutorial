from fastapi import APIRouter

router = APIRouter()

authors = [
    {"id": 1, "name": "author 1", "bio": "author bio"},
    {"id": 2, "name": "author 2", "bio": "author bio"},
    {"id": 3, "name": "author 3", "bio": "author bio"},
]


@router.get("/")
def get_authors(limit: int = 1, skip: int = 0):
    """Get authors from database"""
    response = authors[skip : skip + limit]
    return response


@router.post("/")
def add_author(new_author):
    """Create new author and store in database"""
    authors.append(new_author)

    return authors


@router.get("/{author_id}")
def get_author_by_id(author_id: int):
    """Get single author from database"""
    for author in authors:
        if author["id"] == author_id:
            return author


@router.put("/{author_id}")
def update_author(author_id: int):
    """Update author in database"""
    return {"data": "updated author"}


@router.delete("/{author_id}")
def delete_author(author_id: int):
    """Delete author from database"""
    for author in authors:
        if author["id"] == author_id:
            authors.pop(author_id - 1)

    return authors
