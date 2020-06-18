from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from endpoints import api_blueprint
from flask_jwt_extended import JWTManager

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    app.config['SWAGGER'] = {"title" : "API Prevencao",
                             "uiversion" : 3}
    swagger = Swagger(app)

    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    jwt = JWTManager(app)
    
    app.register_blueprint(api_blueprint, url_prefix="")
    app.run(host='0.0.0.0', port='8090')
