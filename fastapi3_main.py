from fastapi import FastAPI

import fastapi3_routes_post


app = FastAPI()
app.include_router(fastapi3_routes_post.router)


@app.get("/")
def hello_world():
    return {"message": "Hello World!"}
