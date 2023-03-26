from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example from: https://fastapi.tiangolo.com/tutorial/response-model/
# Declaring a custom class for input or output of our enpoint
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


# Receiving and Returing a custom class
@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    return item
