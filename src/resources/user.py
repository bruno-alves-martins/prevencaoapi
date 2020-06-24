from flask_restful import Resource, reqparse
from modelo.userModel import save_to_db, valida_login
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)
parser.add_argument('nome')



class UserRegistration(Resource):

    def post(self):
        """
            Criaçao de usuários
            ---
            operationId: resources.UserRegistration.post
            tags:
                - CreateUser
            description: Endpoint para criação de usuarios
            response:
                200:
            parameters:
                - in: formData
                  name: nome
                  description: Nome do Usuário.
                  required: True
                  type: string
                - in: formData
                  name: username
                  description: Login do Usuário.
                  required: True
                  type: string
                - in: formData
                  name: password
                  description: Senha do usuário.
                  required: True
                  type: string
            responses:
                200:
                    schema:
                        properties:
                            message:
                                type: string
                            
        """
    
        data = parser.parse_args()
   
         
        nome = data['nome']
        username = data['username']
        password = data['password']

       

        try:
           save_to_db(nome, username, password)
           return {
                'message': 'User {} was created'.format( data['username'])
                }
        except:
            return {'message': 'Something went wrong'}, 500



class UserLogin(Resource):

    def post(self):
        data = parser.parse_args()

        username = data['username']
        password = data['password']
    
        if (valida_login(username, password)):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])

            return {
                'message': 'Logged in as {}'.format(username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }

        else: 
            return {'message': 'Wrong credentials'}
