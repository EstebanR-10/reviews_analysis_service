from pymongo import MongoClient
import pandas as pd
from helpers.DateParsers import TripDateToISO8601

class Connection(object):

    __singletonConnection = None
    __client = MongoClient("mongodb+srv://Unicaribe123:Unicaribe123@cluster0.h212q.gcp.mongodb.net/scraping?retryWrites=true&w=majority")
    __datasets = {}
    __db = {}   
    __allowed_collections = ['tripadvisor']

    def __initData(self):
        Connection.__singletonConnection.__db = Connection.__singletonConnection.__getDataBase()
        for dataset in  Connection.__singletonConnection.__allowed_collections:
            Connection.__singletonConnection.__loadDataSets(dataset)
            Connection.__singletonConnection.__prepareDataSet(Connection.__singletonConnection.__datasets[dataset], dataset)

    def __getDataBase(self):
        return self.__client.scraping

    def __loadDataSets(self, name):
        collection = self.__db[name]
        cursor = collection.find({},{ "_id": 0 })
        self.__datasets[name] = (pd.DataFrame(list(cursor)))

    def __prepareDataSet(self,df, nombre):
        #df_tripadvisor = df_tripadvisor.drop([11890,11891])
        sentiment = [0 if int(i)<=20 else 1 if int(i)==30 else 2 for i in df.rating]
        ISO_dates = [TripDateToISO8601(date) for date in df.review_date]
        df['sentiment_label'] = sentiment
        df['review_date'] = pd.to_datetime(ISO_dates)
        df['platform'] = [nombre] * len(df)

    def __str__(self):
        return hex(id(self))

    def getDataSet(self,name: str) -> pd.DataFrame:
        return self.__datasets[name]
    
    def getMergedDataSet(self):
        self.__datasets['tripadvisor'].append(self.__datasets['tripadvisor'], ignore_index=True)
        return self.__datasets['tripadvisor']

    @staticmethod
    def __new__(cls):
        if Connection.__singletonConnection is None:
            Connection.__singletonConnection = object.__new__(cls)
            Connection.__singletonConnection.__initData()

        return Connection.__singletonConnection