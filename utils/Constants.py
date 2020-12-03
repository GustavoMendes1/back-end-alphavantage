import dotenv
import os
import sys

class Constants:
    
    def getParams(symbol):
        return  {'function': 'TIME_SERIES_INTRADAY',
                    'symbol': symbol,
                    'interval': '60min',
                    'apikey': 'YAW95V1UKDSBYXKX'}
        
    def getURL():
        return 'https://www.alphavantage.co/query'
       