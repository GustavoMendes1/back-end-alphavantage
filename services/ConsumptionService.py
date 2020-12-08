from flask import Flask
import json
import requests
from Utils.Constants import Constants as const
from Utils.MessagesExceptions import Messages as msg
from services.DataProcessService import ProcessData

class Consumption:
    
    def getJson(self,symbol,interval):
        try:
            response = requests.request('GET',const.getURL() ,params = const.getParams(symbol,interval))
            
        except:
            return msg.msgError500
        
        if(response.status_code == 200):
            return ProcessData.processData(self,response.json(),interval)    
        else:
            return msg.msgError404

