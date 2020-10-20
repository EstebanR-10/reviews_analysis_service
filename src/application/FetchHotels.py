class FetchHotels:

    def __init__(self, dataFrame, transformer):
        self.dataframe = dataFrame
        self.transformer = transformer

    def process(self):
        return self.transformer.allHotelsList(self.dataframe)