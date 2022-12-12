from typing import Dict, Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, Cyber!"}


# FastAPI will try to match the path pattern one by one, in the oder the paths were defined/configured
@app.get("/blog/all")
def all_blog_page() -> Dict[str, Any]:
    return {"message": f"All blogs!"}


from enum import Enum


class BlogType(str, Enum):
    short = "short"
    long = "long"
    howto = "howto"


# BTW: http://127.0.0.1:8000/docs#/default/get_blog_type_blog_type__blog_type__get
# Will provide ONLY the values that you can use for the function (very cool)
@app.get("/blog/type/{blog_type}")
def get_blog_type(blog_type: BlogType) -> Dict[str, Any]:
    return {
        "message": f"This is blog is of type: {blog_type}, default type: {type(blog_type)}"
    }


# Query params are the 'additinal' parameters that are after the '?' and separated by a '&'
# http://127.0.0.1:8000/blog/query_param_test?query_param1=123&query_param2=abc
@app.get("/blog/query_param_test")
def test_functin(query_param1=123, query_param2="abc"):
    return {"message": f"query_param1: {query_param1}, query_param2: {query_param2}"}


@app.get("/blog/{id}")
def blog_page(id: int) -> Dict[str, Any]:
    return {"message": f"This is blog with ID: {id}, default type: {type(id)}"}


# To run:
# uvicorn fastapi1:app --reload

# Go to docs:
# http://127.0.0.1:8000/docs


# Helpful functinos:
# curl -X 'GET' \
#   'http://127.0.0.1:8000/blog/query_param_test?query_param1=123123&query_param2=abcabc' \
#   -H 'accept: application/json'
