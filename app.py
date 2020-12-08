from flask import Flask
from flask_restful import Resource, Api
from resources.CompaniesResource import Company
from resources.BovespaResource import Bovespa
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)

 
api.add_resource(Bovespa,'/', defaults={'symbol': 'BOVA11.SAO'})
api.add_resource(Company,'/<string:symbol>/<string:interval>')

if __name__ == '__main__':
    app.run(debug=True)