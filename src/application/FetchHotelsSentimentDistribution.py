class FetchHotelsSentimentDistribution:

    def __init__(self, domainService, transformer):
        self.domainService = domainService
        self.transformer = transformer

    def process(self, command):
        params = command.params()
        startDate = params['startDate'] if 'startDate' in params else None
        endDate = params['endDate'] if 'endDate' in params else None

        response =  self.domainService.allHotelsSentimentDistribution(startDate,endDate)
        self.transformer.write(response, params)
        return self.transformer.read()



class Command:

    def __init__(self, params):
        self.aParams = params
    
    def params(self):
        return self.aParams