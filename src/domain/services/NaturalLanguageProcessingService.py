import pandas as pd
from apyori import apriori
from helpers.DataFrame import getColumnWords

class NaturalLanguageProcessingService:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def apriori(self, wordsQuantity: int = None) -> list:
        transactions = getColumnWords(self.df, wordsQuantity)
        association_rules = apriori(transactions, min_support=0.0045, min_confidence=0.5, min_lift=3, min_length=3)
        return self.sortRules(list(association_rules))
    
    def sortRules(self, association_results: list) -> list:
        for i in range(0,len(association_results)-1):
            for j in range(0,len(association_results)-1-i):
                rule = association_results[j]
                if rule[1]<association_results[j+1][1]:
                    association_results[j] = association_results[j+1]
                    association_results[j+1] = rule
        return association_results