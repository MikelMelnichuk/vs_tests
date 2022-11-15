from typing import List, Dict, Any

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

all_items: List[Dict[str, Any]] = []


class Items(Resource):
    def get(self):
        return all_items


class Item(Resource):
    def get(self, name):
        # Take the first item that is found (if any)
        search_item = next(filter(lambda x: x["name"] == name, all_items), None)

        # Return None item, with Error not found (404)
        return {"item": search_item}, 200 if search_item else 404

    def post(self, name):

        # Validation check
        if next(filter(lambda x: x["name"] == name, all_items), None) is not None:
            return {"message": f"Item with name {name} already exists!"}, 400

        user_data = request.get_json()
        new_item = {"name": name, "price": user_data["price"]}
        all_items.append(new_item)

        # 201 -> Created status
        return new_item, 201


api.add_resource(Items, "/items")
api.add_resource(Item, "/item/<string:name>")

# 'debug=True' for better error messages
app.run(port=5000, debug=True)
