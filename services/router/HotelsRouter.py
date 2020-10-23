from flask import Flask
from flask_restful import Resource, Api, marshal_with, marshal, reqparse
from models.Hotel import hotel_resource_fields, Hotel
from config.client.PyMongoConnectionClient import Connection
from src.application.FetchHotels import FetchHotels
from src.application.FetchHotelsByPopularity import FetchHotelsByPopularity
from src.application.FetchHotelsSentimentDistribution import FetchHotelsSentimentDistribution
from src.domain.services.HotelsService import HotelsDomainService
from response import response_resource_fields, Response
from helpers.FilterAdapter import FilterAdapter
from src.application.transformers.HotelTransformer import HotelTransformer

df_tripadvisor = Connection().getDataSet('tripadvisor')
#df_tripadvisor = df_tripadvisor.drop([11890,11891])
sentiment = [0 if int(i)<=20 else 1 if int(i)==30 else 2 for i in df_tripadvisor.rating]
df_tripadvisor['sentiment_label'] = sentiment

class HotelsRouter(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        
        service = FetchHotels(HotelsDomainService(df_tripadvisor))
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)
        
class PopularityRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        parser =  FilterAdapter().parser()
        args = FilterAdapter().adapt()
        service = FetchHotelsByPopularity(HotelsDomainService(df_tripadvisor))
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  [response],  200)

class PopularityDistributionRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        parser =  FilterAdapter().parser()
        args = FilterAdapter().adapt()
        service = FetchHotelsSentimentDistribution(HotelsDomainService(df_tripadvisor), HotelTransformer())
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  [response],  200)
class MainRouter:
    def __init__(self,api):
        self.api = api
    
    def init(self):
        self.api.add_resource(HotelsRouter, '/hotels')
        self.api.add_resource(PopularityRouter, '/hotels/popularity')
        self.api.add_resource(PopularityDistributionRouter, '/hotels/popularity/distribution')
