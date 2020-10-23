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
        rating_dist = self.df.pivot_table(values='rating',index=['hotel_name','sentiment_label'], aggfunc=len)
        return rating_dist