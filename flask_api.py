from flask import Flask, jsonify, request


# Data
stores = [
    {"name": "Store1", "items": [{"name": "item1", "price": 15.99}]},
    {"name": "Store2", "items": [{"name": "item1", "price": 15.99}]},
]

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    post_data = request.get_json()
    new_store = {"name": post_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    post_data = request.get_json()
    for store in stores:
        if store["name"] == post_data["name"]:
            return jsonify(store)
    return jsonify({"message": "Store Wasn't Found!"})


# GET /store
@app.route("/store")
def get_all_stores():
    return jsonify({"stores": stores})


# POST /store/<string:name> data:{name:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    post_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": post_data["name"], "price": post_data["price"]}
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "Store Wasn't Found!"})


# GET /store/<string:name>
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "Item Wasn't Found!"})


app.run(port=5000)
