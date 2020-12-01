from flask import Flask
import json
import requests
from Utils.Constantes import Constantes as const
from Utils.MessagesExceptions import Messages as msg
class Cliente:
    
    def getJson(self,symbol):

        try:
            response = requests.request('GET',const.getURL() ,params = const.getParams(symbol))
        except Exception as e:
            return msg.msgError500

        if(response.status_code == 200):
            return response.json()
        else:
            return msg.msgError404

    def normaliseData():
        pass