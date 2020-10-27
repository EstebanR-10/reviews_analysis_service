class ReviewsCountTransformer:
    __hotel_popularity = {}

    def write(self, df, params = { 'sent': [0,1,2] }):
        if(params):
            for index, value in enumerate(df['rating']):
                sent = df.index.values[index]
                if sent in params['sent']:
                    self.__hotel_popularity[str(sent)] = int(value)
        else:
            self.__hotel_popularity['total'] = int(df.rating.sum())
    
    """
    Metodo encargado de retornar el array de hoteles por popularidad
    """
    def read(self):
        return self.__hotel_popularity