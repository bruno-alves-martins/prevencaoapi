from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from endpoints import api_blueprint

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    app.config['SWAGGER'] = {"title" : "API Prevencao",
                             "uiversion" : 1}
    swagger = Swagger(app)
    app.register_blueprint(api_blueprint, url_prefix="/api")
    app.run(host='localhost', port='8090')
