from flask import Blueprint
from flask_restful import Api
from resources.teste import Teste
from resources.user import UserRegistration, UserLogin


api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

api.add_resource(Teste, "/teste")

api.add_resource(UserRegistration, "/registration")
api.add_resource(UserLogin, "/login")
