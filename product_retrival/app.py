from flask import Flask
from flask_restful import Api

from resources.get_info import Item

app = Flask(__name__)
api = Api(app)

api.add_resource(Item,'/products/<string:Name>')
app.run(host='0.0.0.0', port=5000, debug=True)