
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


# Addition of Tags, makes the '/docs' endpoint much easier to navigate
@app.get('/messages/{id}',
         tags=['messages']
        )  # status_code is the default status-code returned 
def get_all_messages(id: int) -> Dict[str, Any]:
    return {"message": f"Message {id}, default type: {type(id)}"}

@app.get('/messages/{msg_id}/comments/{comment_id}',
         tags=['messages', 'comments']
        )  # status_code is the default status-code returned 
def get_message_comment(msg_id: int, comment_id: int) -> Dict[str, Any]:
    return {"message": f"Message {msg_id}, Comment: {comment_id}"}
