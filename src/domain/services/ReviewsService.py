import pandas as pd

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
