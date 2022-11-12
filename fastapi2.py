
from fastapi import FastAPI, Response, status
from typing import Dict, Any, Optional


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

# Addition of a Summary and Description
@app.get('/func1_with_documentation',
         tags=['documentation'],
         summary="This is the summary of func 1",
         description="This is the description")  # This is the EXPLISIT description
def func1_documentation(var1: int, var2: Optional[str] = None) -> Dict[str, Any]:
    return {'message': f'Var1: {var1}, Var2: {var2}'}

@app.get('/func2_with_documentation',
         tags=['documentation'],
         summary="This is the summary of func 2")
def func2_documentation(var1: int, var2: Optional[str] = None) -> Dict[str, Any]:
    """This description was taken from the DocString of the function in python [INPLICIT Description]


    - var1 (int): integer variable given from the used
    - var2 (Optional[str], optional): A string var like a name. Defaults to None.

    Returns:
        Dict[str, Any]: The result as a JSON string.
    """
    return {'message': f'Var1: {var1}, Var2: {var2}'}
