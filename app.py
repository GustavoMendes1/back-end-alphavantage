from flask import Flask
from flask_restful import Resource, Api
from resources.CompaniesResource import Bovespa,Empresas
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)

 
api.add_resource(Bovespa,'/')
api.add_resource(Empresas,'/<string:symbol>')

if __name__ == '__main__':
    app.run(debug=True)