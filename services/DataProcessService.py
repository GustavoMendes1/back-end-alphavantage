
class ProcessData:
    
    def processData(self,data):
        data = ProcessData.getTimeSeries(self,data)

        newJson = []
        for date in data:
            newJson.append({
                'date': date.split(' ')[0],
                'hour': date.split(' ')[1],
                'points': data[date]['4. close']
            })

        return {'TimeSeries':newJson}

    def getTimeSeries(self,data):
        return data['Time Series (5min)']