from httpx import request

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return jsonify({"message": "Hello World"})



@app.route("/create", methods=["POST"])
def create_item():
    item = request.get_json()
    return {"message": "Item created", "item": item}, 201

@app.route("/update", methods=["PUT"])
def update_item():
    item = request.get_json()
    return {"message": "Item updated", "item": item}, 200   

@app.route("/delete", methods=["DELETE"])
def delete_item():
    item = request.get_json()
    return {"message": "Item deleted", "item": item}, 200

