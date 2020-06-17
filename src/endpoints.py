from flask import Blueprint
from flask_restful import Api
from resources.teste import Teste


api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

api.add_resource(Teste, "/teste")