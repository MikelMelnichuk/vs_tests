from typing import Dict, Any

from fastapi import (
    FastAPI,
    Response,
    status,
)
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()


@app.get(
    "/blog/{id}",
    status_code=status.HTTP_404_NOT_FOUND,
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": r'{"id": 123, "text": "--blog--text--", "comments": ["comment1", "comment2"]}'
                }
            },
            "description": "Returns a blog object using JSON format",
        },
        404: {
            "content": {
                "application/json": {
                    "example": r'{"err_msg": "Error No Bloh with ID 123!"}'
                }
            },
            "description": "Blog not found response",
        },
    },
)  # 'response.status_code' is the default status-code returned
def blog_page(id: int, response: Response) -> Dict[str, Any]:

    if id > 5:
        # Change the return status-code to "Not Found - 404"
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Error No Bloh with ID {id}!"}

    response.status_code = status.HTTP_200_OK
    return {"message": f"Found {id}, default type: {type(id)}"}
