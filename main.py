
from typing import Dict, Any

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"message": "Hello, Cyber!"}

# FastAPI will try to match the path pattern one by one, in the oder the paths were defined/configured
@app.get('/blog/all')
def all_blog_page() -> Dict[str, Any]:
    return {"message": f"All blogs!"}

@app.get('/blog/{id}')
def blog_page(id: int) -> Dict[str, Any]:
    return {"message": f"This is blog with ID: {id}, default type: {type(id)}"}

from enum import Enum
class BlogType(str, Enum):
    short = "short"
    long = "long"
    howto = "howto"

@app.get('/blog/type/{blog_type}')
def get_blog_type(blog_type: BlogType) -> Dict[str, Any]:
    return {"message": f"This is blog is of type: {blog_type}, default type: {type(blog_type)}"}

# To run:
# uvicorn main:app --reload

# Go to docs:
# http://127.0.0.1:8000/docs