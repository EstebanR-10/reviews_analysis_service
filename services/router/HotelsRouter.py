from flask import Flask
from flask_restful import Resource, Api, marshal_with, marshal, reqparse
from models.Hotel import hotel_resource_fields, Hotel
from config.client.PyMongoConnectionClient import Connection
from src.application.FetchHotels import FetchHotels
from src.application.FetchHotelsByPopularity import FetchHotelsByPopularity
from src.domain.services.HotelsService import HotelsDomainService
from response import response_resource_fields, Response

df_tripadvisor = Connection().getDataSet('tripadvisor2')
df_tripadvisor = df_tripadvisor.drop([11890,11891])

class HotelsRouter(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        
        service = FetchHotels(HotelsDomainService(df_tripadvisor))
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)
        
class PopularityRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        service = FetchHotelsByPopularity(HotelsDomainService(df_tripadvisor))
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  [response],  200)
class MainRouter:
    def __init__(self,api):
        self.api = api
    
    def init(self):
        self.api.add_resource(HotelsRouter, '/hotels')
        self.api.add_resource(PopularityRouter, '/hotels/popularity')
