class HotelPopularityTransformer:
    __hotel_popularity = []

    def write(self, df):
        for index, value in enumerate(df[0]):
            self.__hotel_popularity.append( { df.index.values[index]: value } )
    
    def read(self):
        """
        Metodo encargado de retornar el array de hoteles por popularidad
        """
        return self.__hotel_popularity
            
class HotelYearTimeSeriesTransformer:
    __hotel_coment_dist = {}

    def write(self, df, params = { 'sent': [0,1,2] }):
        for hotel, sub_df_hotel in df.groupby(level=0):
            self.__hotel_coment_dist[hotel] = {}
            for sent, sub_df_hotel_sent in sub_df_hotel.groupby(level=1):
                if sent in params['sent']:
                    self.__hotel_coment_dist[hotel][str(sent)] = [int(item) for item in sub_df_hotel_sent.values[0,:]]  

    def read(self):
        return self.__hotel_coment_dist

class HotelPopularityDistributionTransformer:
    __hotel_coment_dist = {}

    def write(self, df, params = { 'sent': [0,1,2] }):
        for hotel, sub_df_hotel in df.groupby(level=0):
            self.__hotel_coment_dist[hotel] = {}
            for sent, sub_df_hotel_sent in sub_df_hotel.groupby(level=1):
                if sent in params['sent']:
                    self.__hotel_coment_dist[hotel][str(sent)] = int(sub_df_hotel_sent.values[0,0])  

    def read(self):
        return self.__hotel_coment_dist
