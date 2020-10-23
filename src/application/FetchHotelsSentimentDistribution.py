class FetchHotelsSentimentDistribution:

    def __init__(self, domainService, transformer):
        self.domainService = domainService
        self.transformer = transformer

    def process(self):
        response =  self.domainService.allHotelsSentimentDistribution()
        self.transformer.write(response)
        return self.transformer.read()