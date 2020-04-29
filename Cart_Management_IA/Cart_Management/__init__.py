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
                x = int(key["quantity"])
                x += 1
                key["quantity"] = str(x)

            return {'message': 'Success', 'data': key}, 201
        return {'message': 'Product not fount', 'data': {}}, 404

    def delete(self, p_id):
        shelf = get_db()

        # If the key does not exist in the data store, return a 404 error.
        if not (p_id in shelf):
            return {'message': 'Product not found', 'data': {}}, 404

        del shelf[p_id]
        return '', 204


api.add_resource(ProductList, '/products')
api.add_resource(Product, '/product/<string:p_id>')
