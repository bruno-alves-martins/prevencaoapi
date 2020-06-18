from flask import request
from flask_restful import Resource
import cx_Oracle
from flask_jwt_extended import (jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)



class Teste(Resource):
    @jwt_required
    def get(self):
        """
            Inseres fotos
            ---
            operationId: resources.AdicionarFoto.post
            tags:
                - AdicionarFoto
            description: Armazena fotos para usar para reconhecimento facial
            response:
                200:
            parameters:
                - in: formData
                  name: foto
                  description: foto a ser armazenada.
                  required: True
                  type: file
                - in: formData
                  name: index
                  description: index da foto.
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

        con = cx_Oracle.connect('hcb_consulta/hcb_consulta@piodb-scan.pioxii.com.br/hcb')
  
                
        print (con.version)

        a = str(con.version)


        return {'oracleversion': a}