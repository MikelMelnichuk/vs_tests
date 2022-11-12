
from fastapi import FastAPI, Response, status
from typing import Dict, Any


app = FastAPI()


@app.get('/blog/{id}', status_code=status.HTTP_404_NOT_FOUND)  # status_code is the default status-code returned 
def blog_page(id: int, response: Response) -> Dict[str, Any]:
    
    if id > 5:
        # Change the return status-code to "Not Found - 404"
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Error No ID: {id} found!"}
    
    response.status_code = status.HTTP_200_OK
    return {"message": f"Found {id}, default type: {type(id)}"}

