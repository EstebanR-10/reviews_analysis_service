import pandas as pd

class HotelsDomainService:
    def __init__(self, df):
        self.df = df

    def allHotelsList(self):
        return self.df.hotel_name.unique()

    def allHotelsByPopularity(self):
        resumen = pd.DataFrame(self.df.groupby(['hotel_name']).size())
        return resumen[0].to_dict()

    def allHotelsSentimentDistribution(self):
        resumen = pd.DataFrame(self.df.groupby(['hotel_name','']).size())
        return resumen[0].to_dict()