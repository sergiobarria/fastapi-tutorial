from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    """Entry path for the application"""
    return {"message": "Hello World"}
