from flask_restful import fields, reqparse, Resource
from flask import request

PRODUCTS = [
    {"Id":"23",
     "Name":"Xbox",
     "Price":"299,00 $",
     "description":"",
     "Seller":"Game&Co",
     "Website":"www.Game&Co.com"
    }
            ]

parser = reqparse.RequestParser()
parser.add_argument('name')

# shows a single item in cart and lets you delete or update an item
class Item(Resource):
    def get(self, Name):
        for record in PRODUCTS:
            if Name == record["Name"]:
                return record, 200
        return {"Place record not found"}, 404