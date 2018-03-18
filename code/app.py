from flask import Flask, request
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
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ReturnAllItems(Resource):
    def get(self):
        return {'Items': items}, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ReturnAllItems, '/items')

app.run(port = 4000, debug=True)
