from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            print('here in the loop')
            if item['name'] == name:
                print('here in the if statment')
                return item
        return {'item': 'Does not exit in the database'}, 404

    def post(self, name):
        item = {'name': name, 'price': 12}
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<string:name>')

app.run(port = 4000)
