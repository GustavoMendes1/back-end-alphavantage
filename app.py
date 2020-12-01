from flask import Flask
from flask_restful import Resource, Api
from resources.EmpresasResource import Bovespa,Empresas

app = Flask(__name__)
api = Api(app)
        
api.add_resource(Bovespa,'/')
api.add_resource(Empresas,'/<string:symbol>')

if __name__ == '__main__':
    app.run(debug=True)