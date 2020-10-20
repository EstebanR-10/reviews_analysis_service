class HotelsTransformer:
    def allHotelsList(self, df):
        return df.hotel_name.unique()