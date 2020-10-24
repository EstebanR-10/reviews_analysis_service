class HotelTransformer:
    __hotel_coment_dist = {}

    def write(self, df, params = { 'sent': [0,1,2] }):
        for hotel, sub_df_hotel in df.groupby(level=0):
            self.__hotel_coment_dist[hotel] = {}
            for sent, sub_df_hotel_sent in sub_df_hotel.groupby(level=1):
                if sent in params['sent']:
                    self.__hotel_coment_dist[hotel][str(sent)] = [int(item) for item in sub_df_hotel_sent.values[0,:]]  

    def read(self):
        return self.__hotel_coment_dist

