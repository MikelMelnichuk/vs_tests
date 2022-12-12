from typing import Optional


from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])

# Declaring a custom class for input or output of our enpoint
class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


# This functin contains all 3 types of parameters:
# 1) blog - Json data from the body of the request
# 2) id - This is a path parameter
# 3) version - This is a Query parameter
@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"id": id, "version": version, "blog": blog}


@router.post("/new/{id}/validators")
def create_blog_validators(
    blog: BlogModel,
    id: int,
    version: int = Query(
        default=None,
        title="Some Title for the parameter in Docs",
        description="This is a description to Docs",
    ),
    testsss: str = Body(default=..., min_length=5, max_length=10, regex="^[a-z ]*$"),
):
    return {"id": id, "version": version, "blog": blog, "testsss": testsss}
