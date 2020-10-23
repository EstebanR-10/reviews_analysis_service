from pymongo import MongoClient
import pandas as pd

class Connection(object):

    __singletonConnection = None
    __client = MongoClient("mongodb+srv://Unicaribe123:Unicaribe123@cluster0.h212q.gcp.mongodb.net/scraping?retryWrites=true&w=majority")
    __datasets = {}

    def __init__(self):
        self.db = self.__getDataBase()
        self.__loadDataSets('tripadvisor')

    def __getDataBase(self):
        return self.__client.scraping

    def __loadDataSets(self,name):
        collection = self.db[name]
        cursor = collection.find({},{ "_id": 0 })
        self.__datasets[name] = (pd.DataFrame(list(cursor)))

    def getDataSet(self,name):
        return self.__datasets[name]

    @staticmethod
    def __new__(cls):
        if Connection.__singletonConnection is None:
            Connection.__singletonConnection = object.__new__(cls)
        return Connection.__singletonConnection