class FetchHotelsByPopularity:

    def __init__(self, domainService, trasnformer):
        self.domainService = domainService
        self.transformer = trasnformer

    def process(self):
        self.transformer.write(self.domainService.allHotelsByPopularity())
        return self.transformer.read()