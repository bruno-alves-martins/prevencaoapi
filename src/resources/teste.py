from flask import request
from flask_restful import Resource



class Teste(Resource):
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



        return {'hello': 'Teste de Api Prevencao'}