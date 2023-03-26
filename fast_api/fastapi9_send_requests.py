from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str


@app.post("/")
async def root(data: Item):
    return {"message": f"You wrote: '{data.text}'"}


# ------------------------------------------------------------------------------------------------------------

import requests

res = requests.post(
    "http://localhost:8000/",
    headers={
        #'User-agent'  : 'Internet Explorer/2.0',
        "Content-type": "application/json"
    },
    json={"text": "Fast API"},
)
# print(res.headers['content-type'])
print(res.text)

# Send get request to "fastapi8_what_to_test:app"
url = "http://127.0.0.1:8000/items/foo"  # The Path-Variable 'item_id'=foo [withing the /items/ endpoint]
res = requests.get(
    url, headers={"X-Token": "coneofsilence"}
)  # Query-Variable 'x_token'=coneofsilence

print(res.status_code)
print(res.json())
