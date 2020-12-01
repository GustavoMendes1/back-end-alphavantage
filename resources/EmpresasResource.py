
from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.Cliente import Cliente


class Bovespa(Resource):
    def get(self,symbol="IBM"):
        
        return Cliente().getJson(symbol)

class Empresas(Resource):

    def get(self,symbol):
        return Cliente().getJson(symbol)