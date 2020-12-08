from Utils.MessagesExceptions import Messages as msg
import re
class ProcessData:
    
    def processData(self,data,interval):
        try:
            data = ProcessData.getTimeSeries(self,data,interval)
        except:
            return msg.msgError404

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

    def getTimeSeries(self,data,interval):
        if interval is None:
            return data['Time Series (Daily)']
        else:
            return data['Time Series ('+interval+')']
        