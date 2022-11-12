
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return "Hello, Cyber!"


# To run:
# uvicorn main:app --reload

# Go to docs:
# http://127.0.0.1:8000/docs#/default/index__get