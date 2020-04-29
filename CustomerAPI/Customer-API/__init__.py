import os
import shelve

# Import the framework
from flask import Flask, g, render_template
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("customers.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template('index.html')

class Customers(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        customers = []

        for key in keys:
            customers.append(shelf[key])

        return {'message': 'Customers:', 'data': customers}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('customer_id', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('address', required=True)
        parser.add_argument('zipcode', required=True)
        parser.add_argument('City', required=True)
        parser.add_argument('email', required=True)
        #parser.add_argument('orders_placed', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        keys = list(shelf.keys())
                        
        shelf[args['customer_id']] = args

        return {'message': 'Customer created', 'data': args}, 201

class Customer(Resource):
    def get(self, customer_id):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (customer_id in shelf):
            return {'message': 'Customer not found', 'data': {}}, 404

        return {'message': 'Customer found', 'data': shelf[customer_id]}, 200

    def delete(self, customer_id):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (customer_id in shelf):
            return {'message': 'Customer not found', 'data': {}}, 404

        del shelf[customer_id]
        return 'Product removed from cart', 204


api.add_resource(Customers, '/customers')
api.add_resource(Customer, '/customer/<string:customer_id>')
