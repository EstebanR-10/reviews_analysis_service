class FetchHotelsSentimentDistribution:

    def __init__(self, domainService, transformer):
        self.domainService = domainService
        self.transformer = transformer

    def process(self, command):
        response =  self.domainService.allHotelsSentimentDistribution()
        self.transformer.write(response, command.params())
        return self.transformer.read()



class Command:

    def __init__(self, params):
        self.aParams = params
    
    def params(self):
        return self.aParams