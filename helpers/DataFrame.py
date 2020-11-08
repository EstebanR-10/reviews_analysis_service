import pandas as pd
import re
from helpers.BagOfWords import stopwords

detected_stop = ['lagunamar', 't', 'oasis', 'fiesta', 'consesa', 'americana', 'grand', 'telmo', 'san', 'wi','fi', 'hotel']

###
# Función encargada de convertir una columna de un dataframe en una lista de listas con las palabras de cada fila.
# @param pandas.DataFrame 'df' dataframe
# @return List 'transactions' 
###
def getColumnWords(df: pd.DataFrame, size: int = None, hotels: list = None) -> list:
    
    if hotels:
        df = df[df['hotel_name'].isin(hotels)]

    transactions = []
    for review in df.review_body:
        tokens = re.findall(r'\w+|\d+',review)
        alpha_lower = [token.lower() for token in tokens if token.isalpha()]
        transactions.append([t for t in alpha_lower if t not in stopwords['spanish'] if t not in stopwords['english'] if t not in detected_stop])
    if(size):
        short_transactions = []
        for item in transactions:
            short_transactions.append(item[:size])
        transactions = short_transactions
    return transactions