import os

class ReviewsService:
    directory = ''
    filename = 'reviews.xlsx'
    def __init__(self, df):
        self.df = df
        self.directory = os.getcwd() + "/resources/"

    """
    Descripción: Método encargado de crear un archivo en formato xmls para su manejo en word.
    @return object
    """
    def allReviewsXmls(self):
        self.df.to_excel(self.directory + self.filename, index=False)
        return { 'directory': self.directory, 'filename': self.filename }
