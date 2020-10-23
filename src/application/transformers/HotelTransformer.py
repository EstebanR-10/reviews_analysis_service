class HotelTransformer:
    hotel_coment_dist = {}

    def write(self, df):
        for hotel, sub_df_hotel in df.groupby(level=0):
            self.hotel_coment_dist[hotel] = {}
            for sent, sub_df_hotel_sent in sub_df_hotel.groupby(level=1):
                self.hotel_coment_dist[hotel][str(sent)] = int(sub_df_hotel_sent.values[0,0])  

    def read(self):
        return self.hotel_coment_dist

