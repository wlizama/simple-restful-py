from flask_restful import Resource, reqparse
from Data import users


class UserList(Resource):

    def get(self):
        return {"users": users}


class User(Resource):

    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
        
        return "User no found", 404


    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("ocupation")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                return "User with name %s alredy exists" % name, 400
        
        user = {
            "name": name,
            "age": args["age"],
            "ocupation": args["ocupation"]
        }
        users.append(user)
        return user, 201


    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("ocupation")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                user["age"] = args["age"]
                user["ocupation"] = args["ocupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "ocupation": args["ocupation"]
        }
        users.append(user)
        return user, 201

    
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "%s has been deleted" % name, 200
    