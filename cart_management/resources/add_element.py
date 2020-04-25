from flask_restful import fields, marshal_with, reqparse, Resource
from flask import request

CART = list()


parser = reqparse.RequestParser()
parser.add_argument('name')

# shows a single item in cart and lets you delete or update an item
class Item(Resource):
    def get(self, name):
        for record in CART:
            if name == record["name"]:
                return record, 200
        return {"Place record not found"}, 404

    def delete(self, name):
        for record in CART:
            if name == record["name"]:
                CART.pop(CART.index(record))
                return '', 204
        return "Item not found in cart"

    def put(self, name):
        record_to_be_created = request.get_json(force=True)
        name = record_to_be_created['name']
        quantity = record_to_be_created["quantity"]
        for record in CART:
            if name == record["name"]:
                record['quantity']=quantity
        return record, 201


# TodoList
# shows a list of all items in cart, and lets you POST to add new item
class cartList(Resource):
    def get(self):
        return CART

    def post(self):
        record_to_be_created = request.get_json(force=True)
        name = record_to_be_created["name"]
        for record in CART:
            if name == record["name"]:
                record["quantity"] += 1
        CART.append(record_to_be_created)
        return record_to_be_created, 201

