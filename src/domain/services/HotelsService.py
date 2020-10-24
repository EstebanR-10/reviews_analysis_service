import pandas as pd

class HotelsDomainService:
    def __init__(self, df):
        self.df = df

    def allHotelsList(self):
        return self.df.hotel_name.unique().tolist()

    def allHotelsByPopularity(self):
        resumen = pd.DataFrame(self.df.groupby(['hotel_name']).size())
        resumen = resumen.sort_values(by=0, ascending=False)
        return resumen[0].to_dict()

    def allHotelsSentimentDistribution(self):
        rating_dist = self.df.pivot_table(values='rating',index=['hotel_name','sentiment_label'], aggfunc=len)
        return rating_dist

    def allHotelsSentimentDistributionTimeSeries(self):
        hotel_coment_year_dist = {}

        self.df['date']=self.df['review_date'].dt.year
        pivot = self.df.pivot_table(values='review_body',index=['hotel_name','sentiment_label'], columns='date', aggfunc=len).fillna(0)
        
        return pivot
        #for hotel, sub_df_hotel in df.groupby(level=0):
        #    self.hotel_coment_year_dist[hotel] = {}
         #   for sent, sub_df_hotel_sent in sub_df_hotel.groupby(level=1):
          #          self.__hotel_coment_dist[hotel][str(sent)] = int(sub_df_hotel_sent.values[0,:])  
           #         return pivot..to_dict()