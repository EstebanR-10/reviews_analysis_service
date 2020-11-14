import pandas as pd
from datetime import datetime 

class HotelsDomainService:
    def __init__(self, df):
        self.df = df

    def allHotelsList(self):
        return self.df.hotel_name.unique().tolist()

    def allHotelsByPopularity(self):
        resumen = pd.DataFrame(self.df.groupby(['hotel_name']).size())
        resumen = resumen.sort_values(by=0, ascending=False)
        return resumen

    def allHotelsSentimentDistribution(self, startDate: datetime, endDate: datetime):
        if startDate and endDate:
            self.df = self.df[(self.df['review_date'] >= startDate) & (self.df['review_date'] <= endDate)]
        rating_dist = self.df.pivot_table(values='rating',index=['hotel_name','sentiment_label'], aggfunc=len)
        return rating_dist

    def allHotelsSentimentDistributionTimeSeries(self, startDate: datetime, endDate: datetime):
        self.df['date']=self.df['review_date'].dt.year        
        if startDate and endDate:
            self.df = self.df[(self.df['date'] >= startDate.year) & (self.df['date'] <= endDate.year)]
        pivot = self.df.pivot_table(values='review_body',index=['hotel_name','sentiment_label'], columns='date', aggfunc=len).fillna(0)
        return pivot

    def allHotelsSentimentMonthDistributionTimeSeries(self, startDate: datetime, endDate: datetime):
        self.df['month']=self.df['review_date'].dt.to_period('M')
        if startDate and endDate:
            self.df = self.df[(self.df['review_date'] >= startDate) & (self.df['review_date'] <= endDate)]
        pivot = self.df.pivot_table(values='review_body',index=['hotel_name','sentiment_label'], columns='month', aggfunc=len).fillna(0)
        return pivot