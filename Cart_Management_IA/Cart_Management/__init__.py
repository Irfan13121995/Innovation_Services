import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("products.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/Readme.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class ProductList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        products = []

        for key in keys:
            products.append(shelf[key])

        return {'message': 'Success', 'data': products}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('p_id', required=True)
        parser.add_argument('p_type', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('quantity', required=True)

        # Parse the arguments into an object
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['p_id']] = args

        return {'message': 'product added to cart', 'data': args}, 201

class Product(Resource):
    def get(self, p_id):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (p_id in shelf):
            return {'message': 'Product not found', 'data': {}}, 404

        return {'message': 'Product found', 'data': shelf[p_id]}, 200

    def put(self, p_id):
        shelf = get_db()
        keys = list(shelf.keys())
        for key in keys:
            if key["p_id"] == p_id:
                key["quantity"] += 1

            return {'message': 'Success', 'data': shelf[p_id]}, 201
        return {'message': 'Product not fount', 'data': {}}, 404

    def delete(self, p_id):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (p_id in shelf):
            return {'message': 'Product not found', 'data': {}}, 404

        del shelf[p_id]
        return '', 204


api.add_resource(ProductList, '/products')
api.add_resource(Product, '/product/<integer:p_id>')
