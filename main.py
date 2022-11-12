
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"message": "Hello, Cyber!"}


@app.get('/blog/{id}')
def blog_page(id):
    return {"message": f"This is blog with ID: {id}, default type: {type(id)}"}


# To run:
# uvicorn main:app --reload

# Go to docs:
# http://127.0.0.1:8000/docs