
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