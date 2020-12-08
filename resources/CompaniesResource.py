
from flask import Flask
from flask_restful import Resource, Api, reqparse
from services.ConsumptionService import Consumption

class Company(Resource):

    def get(self,symbol, interval):
        return Consumption().getJson(symbol,interval)