
class Constants:
    
    def getParamsCompanies(symbol, interval):
        return  {'function': 'TIME_SERIES_INTRADAY',
                    'symbol': symbol,
                    'interval': interval,
                    'apikey': 'YAW95V1UKDSBYXKX'}
        
    def getURL():
        return 'https://www.alphavantage.co/query'

    def getParamsBovespa(symbol):
        return  {'function': 'TIME_SERIES_DAILY',
                    'symbol': symbol,
                    'apikey': 'YAW95V1UKDSBYXKX'}
    
  
       