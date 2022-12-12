from fastapi import (
    FastAPI,
    Query,
    Body,
    status,
)
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

live = False
if live:
    from transformers import pipeline

    classifier = pipeline("sentiment-analysis")


# Made for convenience
@app.get("/", response_class=HTMLResponse, name="homepage")
def home_func():
    return RedirectResponse(
        app.url_path_for(name="homepage") + "docs",
        status_code=status.HTTP_303_SEE_OTHER,
    )


@app.get("/query_example", tags=["GET"])
def query_example(
    user_comment: str = Query(
        ..., description="This is the comment we want to find it's sentiment"
    )
):
    return {"text": classifier(user_comment) if live else user_comment}


@app.post("/body_example", tags=["POST"])
def body_example(user_comment: str = Body(..., description="This is a Body parameter")):
    return {"text": classifier(user_comment) if live else user_comment}
