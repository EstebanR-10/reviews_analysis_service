from flask import Flask
from flask_restful import Resource, Api, marshal_with, marshal
from models.Hotel import hotel_resource_fields, Hotel
from config.client.PyMongoConnectionClient import Connection
from src.application.FetchHotels import FetchHotels
from src.application.transformers.HotelsTransformer import HotelsTransformer
from response import response_resource_fields, Response

df_tripadvisor = Connection().getDataSet('tripadvisor2')
df_tripadvisor = df_tripadvisor.drop([11890,11891])

class HotelsRouter(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        
        service = FetchHotels(df_tripadvisor, HotelsTransformer())
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)
        

