
class Constants:
    
    def getParams(symbol, interval):
        return  {'function': 'TIME_SERIES_INTRADAY',
                    'symbol': symbol,
                    'interval': interval,
                    'apikey': 'YAW95V1UKDSBYXKX'}
        
    def getURL():
        return 'https://www.alphavantage.co/query'
       