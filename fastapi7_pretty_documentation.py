from fastapi import FastAPI
from pydantic import BaseModel, Field


# some documentation in markdown
description = """
## Documentation
**ℹ️ Read carefully before using ℹ️**

This api allows you to predict the type of Iris plant given a list of features.
The features should be:
* sepal length in cm
* sepal width in cm
* petal length in cm
* petal width in cm

_Build by:_
![logo](<https://amplemarket.com/_next/image?url=%2Fsvg%2Flogo.svg&w=384&q=75>)
"""

# create FastAPI app and load model
app = FastAPI(
    title="IRIS Classification",
    description=description,
    version="0.1",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/")
def home_page():
    return {"status": "All good!"}


# We'll take this in:
class Features(BaseModel):
    sepal_length: float = Field(..., ge=0.0, le=1.0)
    sepal_width: float = Field(..., ge=0.0, le=1.0)
    petal_length: float = Field(..., ge=0.0, le=1.0)
    petal_width: float = Field(..., ge=0.0, le=1.0)

    # with an example
    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 0.2,
                "sepal_width": 0.5,
                "petal_length": 0.8,
                "petal_width": 1.0,
            }
        }


# We'll respond something like this:
class Response(BaseModel):
    setosa_probability: float = Field(..., ge=0.0, le=1.0)
    versicolor_probability: float = Field(..., ge=0.0, le=1.0)
    virginica_probability: float = Field(..., ge=0.0, le=1.0)

    # with an example
    class Config:
        schema_extra = {
            "example": {
                "setosa_probability": 0.7,
                "versicolor_probability": 0.1,
                "virginica_probability": 0.2,
            }
        }


# the endpoint
@app.post("/predict/", response_model=Response)
def predict(features: Features) -> Response:
    feature_list = [
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.sepal_width,
    ]
    # predictions = model.predict_proba([feature_list])[-1]
    predictions = [0.1, 0.2, 0.3]
    predictions_clean = Response(
        setosa_probability=predictions[0],
        versicolor_probability=predictions[1],
        virginica_probability=predictions[2],
    )
    return predictions_clean
