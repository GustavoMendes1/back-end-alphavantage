from flask import Flask
import json
import requests
from utils.Constants import Constants as const
from utils.MessagesExceptions import Messages as msg
from services.DataProcessService import ProcessData

class Consumption:
    
    def getJson(self,symbol,interval):
        try:
            if interval is None:
                params = const.getParamsBovespa(symbol)
            else:
                 params = const.getParamsCompanies(symbol,interval)
            response = requests.request('GET', const.getURL(), params=params)   
        except:
            return msg.msgError500
        
        if(response.status_code == 200):       
            return ProcessData.getTimeSeries(self, response.json(), interval)    
        else:
            return msg.msgError404
    
    

