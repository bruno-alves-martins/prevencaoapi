from flask_restful import Resource
from modelo.mamografiaModel import getProdMmgMensalCC, getProdMmgSemanaCC, getProdMmgMediaDiaSemana, getProdMmgDiariaCC
from flask import request
import json
import locale
from flask_jwt_extended import (jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

class ProdMmgMensalCC(Resource):
    @jwt_required
    def post(self):
        """
            Busca Mamografias no Ano por centro de custo
            ---
            operationId: resources.ProdMmgMensalCC.post
            tags:
                - ProducaoMamografiaCentroCusto
            description: Endpoint retorna a quantidade por mes de mamografia realizada no ano informado e no ano anterior
            response:
                200:
            parameters:
                - in: text
                  name: ano1
                  description: ano atual.
                  required: True
                  type: string
                - in: text
                  name: ano2
                  description: ano anterior.
                  required: True
                  type: string
                - in: text
                  name: centrocusto
                  description: centro de custo de pesquisa.
                  required: True
                  type: string
            responses:
                200:
                    schema:
                        properties:
                            status:
                                type: string
                            result:
                                type: string
        """
        ret_dict = {}
        json_data = request.get_json(force=True)
        print(json_data)
        ano1 = json_data['ano1']
        ano2 = json_data['ano2']
        centrocusto = json_data['centrocusto']

        result = getProdMmgMensalCC(ano1, ano2, centrocusto)

        return  { "status": 'success', "result" : result}, 200


class ProdMmgSemanalCC(Resource):
    
    def post(self):
        """
            Busca Mamografias no Ano por centro de custo
            ---
            operationId: resources.ProdMmgMensalCC.post
            tags:
                - ProducaoMamografiaCentroCusto
            description: Endpoint retorna a quantidade por mes de mamografia realizada no ano informado e no ano anterior
            response:
                200:
            parameters:
                - in: text
                  name: ano1
                  description: ano atual.
                  required: True
                  type: string
                - in: text
                  name: ano2
                  description: ano anterior.
                  required: True
                  type: string
                - in: text
                  name: centrocusto
                  description: centro de custo de pesquisa.
                  required: True
                  type: string
            responses:
                200:
                    schema:
                        properties:
                            status:
                                type: string
                            result:
                                type: string
        """
        ret_dict = {}
        json_data = request.get_json(force=True)
        print(json_data)
        ano = json_data['ano']
        mes = json_data['mes']
        centrocusto = json_data['centrocusto']

        result = getProdMmgSemanaCC(ano, mes, centrocusto)

        return  { "status": 'success', "result" : result}, 200



class ProdMmgMediaDiaSemanaCC(Resource):
    
    def post(self):
        """
            Media de mamografia realizada por dia da semana
            ---
            operationId: resources.ProdMmgMensalCC.post
            tags:
                - ProducaoMamografiaCentroCusto
            description: Endpoint retorna a quantidade por mes de mamografia realizada no ano informado e no ano anterior
            response:
                200:
            parameters:
                - in: text
                  name: ano1
                  description: ano atual.
                  required: True
                  type: string
                - in: text
                  name: ano2
                  description: ano anterior.
                  required: True
                  type: string
                - in: text
                  name: centrocusto
                  description: centro de custo de pesquisa.
                  required: True
                  type: string
            responses:
                200:
                    schema:
                        properties:
                            status:
                                type: string
                            result:
                                type: string
        """
        ret_dict = {}
        json_data = request.get_json(force=True)
        print(json_data)
        ano = json_data['ano']
        centrocusto = json_data['centrocusto']

        result = getProdMmgMediaDiaSemana(ano, centrocusto)

        return  { "status": 'success', "result" : result}, 200

class ProdMmgDiariaCC(Resource):
    
    def post(self):
        """
            Busca Mamografias no Ano e no mes por dia
            ---
            operationId: resources.ProdMmgMensalCC.post
            tags:
                - ProducaoMamografiaCentroCusto
            description: Endpoint retorna a quantidade por mes de mamografia realizada no ano informado e no ano anterior
            response:
                200:
            parameters:
                - in: text
                  name: ano1
                  description: ano atual.
                  required: True
                  type: string
                - in: text
                  name: ano2
                  description: ano anterior.
                  required: True
                  type: string
                - in: text
                  name: centrocusto
                  description: centro de custo de pesquisa.
                  required: True
                  type: string
            responses:
                200:
                    schema:
                        properties:
                            status:
                                type: string
                            result:
                                type: string
        """
        ret_dict = {}
        json_data = request.get_json(force=True)
        print(json_data)
        ano = json_data['ano']
        mes = json_data['mes']
        centrocusto = json_data['centrocusto']

        result = getProdMmgDiariaCC(ano, mes, centrocusto)

        return  { "status": 'success', "result" : result}, 200

