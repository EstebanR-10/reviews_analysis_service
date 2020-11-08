import pandas as pd
from helpers.BagOfWords import BagOfWords, stopwords, detected_stop
class ReviewsDomainService:
    def __init__(self, df):
        self.df = df

    """
    Descripción: Método encargado de filtrar y devolver las reviews disponibles del dataset.
    @return List
    """
    def allReviewsList(self):
        return self.df.review_body.tolist()

    """
    Método encargado de devolver el número total de reviews disponibles en el dataset
    """
    def allReviewsCount(self):
        reviews_size = self.df.pivot_table(values='rating',index=['sentiment_label'], aggfunc=len)
        return reviews_size
    
    def wordsFrequency(self):
        bow_df = BagOfWords(self.df, set(stopwords['english']).union(set( stopwords['spanish'])).union(set(detected_stop)))
        word_freq = bow_df.sum().sort_values(ascending=False)
        return word_freq
