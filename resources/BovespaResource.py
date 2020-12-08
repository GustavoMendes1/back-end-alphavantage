from flask import Flask
from flask_restful import Resource, Api, reqparse
from services.ConsumptionService import Consumption

class Bovespa(Resource):

    def get(self,symbol):
        return Consumption().getJson(symbol,None)