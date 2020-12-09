from Utils.MessagesExceptions import Messages as msg
import re
class ProcessData:
    

    def processDataCompany(self,data):
        newJson = []
        for position in data:
            time = (re.findall("[0-9]{2}:[0-9]{2}", position)[0])
            date = (re.findall("[0-9]{2}-[0-9]{2} ", position)[0])
            date = date.replace("-", "/")
            dateTime = time +" "+ date
            
            newJson.append({
                'dateTime':dateTime,
                'points': data[position]['4. close']
            })

        return {'data':newJson}

    def processDataBovespa(self,data):
        newJson = []
        for position in data:
            date = (re.findall("-[0-9]{2}-[0-9]{2}", position)[0])
            date = date.replace("-", "/")
            date = date[1:]

            newJson.append({
                'dateTime':date,
                'points': data[position]['4. close']
            })

        return {'data':newJson}
    
    def getTimeSeries(self,data,interval):
        try:
            if interval is None:
                return ProcessData.processDataBovespa(self,data['Time Series (Daily)'])
            else:
                return ProcessData.processDataCompany(self,data['Time Series ('+interval+')'])
        except:
            return msg.msgError404