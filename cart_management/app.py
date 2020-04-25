from flask import Flask
from flask_restful import Api

from resources.add_element import Item, cartList

app = Flask(__name__)
api = Api(app)

api.add_resource(cartList,'/placerecords')
api.add_resource(Item, '/placerecords/<string:name>')

app.run(host='0.0.0.0', port=5000, debug=True)