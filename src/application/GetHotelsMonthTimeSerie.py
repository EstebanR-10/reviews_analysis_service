from src.domain.services.HotelsService import HotelsDomainService
from src.application.transformers.HotelTransformer import HotelYearTimeSeriesTransformer

"""
Caso de uso para obtener los datos de graficación para una 
serie de tiempo del número de reviews por mes de cada hotel.
"""
class GetHotelsMonthTimeSerie:

    def __init__(self, domainService: HotelsDomainService, transformer: HotelYearTimeSeriesTransformer):
        self.domainService = domainService
        self.transformer = transformer

    def process(self, command):
        params = command.params()
        startDate = params['startDate'] if 'startDate' in params else None
        endDate = params['endDate'] if 'endDate' in params else None

        df = self.domainService.allHotelsSentimentMonthDistributionTimeSeries(startDate, endDate)
        self.transformer.write(df, params)
        return self.transformer.read()

class Command:

    def __init__(self, params: dict):
        self.aParams = params
    
    def params(self) -> dict:
        return self.aParams