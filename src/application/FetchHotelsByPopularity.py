class FetchHotelsByPopularity:

    def __init__(self, domainService):
        self.domainService = domainService

    def process(self):
        return self.domainService.allHotelsByPopularity()