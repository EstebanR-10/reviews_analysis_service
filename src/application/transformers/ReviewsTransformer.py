class ReviewsCountTransformer:
    __hotel_popularity = {}

    def write(self, df, params = None):
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

class WordFrequencyTrasnformer:
        
    def __init__(self):
        self.__words_frequency = []

    def write(self, df):
         for index, value in enumerate(df):
            self.__words_frequency.append({
                'text': df.index.values[index], 
                'value': int(value) 
                })
                
    def read(self):
        return self.__words_frequency