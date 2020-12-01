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
        data = ProcessData.getTimeSeries(self,data)

        newJson = []
        for date in data:
            newJson.append({
                'data': date.split(' ')[0],
                'hora': date.split(' ')[1],
                'valor': data[date]['4. close']
            })

        return {'Valores':newJson}

    def getTimeSeries(self,data):
        return data['Time Series (60min)']