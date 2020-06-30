from flask import Blueprint
from flask_restful import Api
from resources.teste import Teste
from resources.user import UserRegistration, UserLogin
from resources.mamografia import ProdMmgMensalCC, ProdMmgSemanalCC, ProdMmgMediaDiaSemanaCC, ProdMmgDiariaCC


api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

api.add_resource(Teste, "/teste")

api.add_resource(UserRegistration, "/registration")
api.add_resource(UserLogin, "/login")

api.add_resource(ProdMmgMensalCC , "/getmmganual")
api.add_resource(ProdMmgSemanalCC, "/getmmgsemanal")
api.add_resource(ProdMmgMediaDiaSemanaCC,  "/getmmgmediasemana")
api.add_resource(ProdMmgDiariaCC, "/getmmgdiaria")
