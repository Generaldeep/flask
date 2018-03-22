from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ReturnAllItems

app = Flask(__name__)
app.secret_key = 'thisisasecretykey'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ReturnAllItems, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == 'main':
    app.run(port = 4000, debug=True)
