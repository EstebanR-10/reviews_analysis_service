from pymongo import MongoClient
import pandas as pd

class Connection():

    client = MongoClient("mongodb+srv://Unicaribe123:Unicaribe123@cluster0.h212q.gcp.mongodb.net/scraping?retryWrites=true&w=majority")

    def __init__(self):
        self.db = self.getDataBase()
      
    def getDataBase(self):
        return self.client.scraping

    def getDataSet(self,name):
        collection = self.db[name]
        cursor = collection.find({},{ "_id": 0 })
        return pd.DataFrame(list(cursor))