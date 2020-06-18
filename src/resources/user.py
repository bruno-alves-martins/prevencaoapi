from flask_restful import Resource, reqparse
from model.userModel import save_to_db, valida_login
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


parser = reqparse.RequestParser()



class UserRegistration(Resource):
    
    parser.add_argument('username', help = 'Campo username nao deve ficar em branco', required = True)
    parser.add_argument('password', help = 'Campo password nao deve ficar em branco', required = True)


    def post(self):
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
    parser.add_argument('username', help = 'Campo username nao deve ficar em branco', required = True)
    parser.add_argument('password', help = 'Campo password nao deve ficar em branco', required = True)
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
