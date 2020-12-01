from flask import Flask
import json
import requests
from Utils.Constantes import Constantes as const
from Utils.MessagesExceptions import Messages as msg

class Cliente:
    
    def getJson(self,symbol):

        try:
            response = requests.request('GET',const.getURL() ,params = const.getParams(symbol))
        except:
            return msg.msgError500

        if(response.status_code == 200):
            return ProcessData.processData(self,response.json())    
        else:
            return msg.msgError404

class ProcessData:
    def processData(self,data):
        return data['Time Series (60min)']


    