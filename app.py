from flask import Flask
from flask_restful import Api, Resource, reqparse
from User import UserList, User

app = Flask(__name__)
api = Api(app)

api.add_resource(UserList, "/users")
api.add_resource(User, "/users/<string:name>")
app.run(debug=True)