from Utils.MessagesExceptions import Messages as msg
import re
class ProcessData:
    
    def processData(self,data):
        try:
            data = ProcessData.getTimeSeries(self,data)
        except:
            return msg.msgError404

        newJson = []
        for date in data:
            dateTime = re.findall("[0-9]{2}:[0-9]{2}", date)[0] \
            +" "+re.findall("[0-9]{2}-[0-9]{2}", date)[0]
            newJson.append({
                'dateTime':dateTime,
                'points': data[date]['4. close']
            })

        return {'data':newJson}

    def getTimeSeries(self,data):
        return data['Time Series (5min)']