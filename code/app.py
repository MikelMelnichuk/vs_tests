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
        search_result = [item for item in all_items if item["name"] == name]

        # Return the item if found
        if search_result:
            return search_result[0]

        # Return None item, with Error not found (404)
        return {"item": None}, 404

    def post(self, name):
        user_data = request.get_json()
        new_item = {"name": name, "price": user_data["price"]}
        all_items.append(new_item)

        # 201 -> Created status
        return new_item, 201


api.add_resource(Items, "/items")
api.add_resource(Item, "/item/<string:name>")

# 'debug=True' for better error messages
app.run(port=5000, debug=True)
