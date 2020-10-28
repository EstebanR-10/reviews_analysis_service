from flask import Flask
from flask_restful import Resource, Api, marshal_with, marshal, reqparse
from models.Hotel import hotel_resource_fields, Hotel
from config.client.PyMongoConnectionClient import Connection
from src.application.FetchHotels import FetchHotels
from src.application.FetchHotelsByPopularity import FetchHotelsByPopularity
from src.application.FetchHotelsSentimentDistribution import FetchHotelsSentimentDistribution, Command as FetchHotelsSentimentDistributionCommand
from src.domain.services.HotelsService import HotelsDomainService
from response import response_resource_fields, Response
from helpers.FilterAdapter import FilterAdapter
from src.application.transformers.HotelTransformer import HotelPopularityTransformer, HotelPopularityDistributionTransformer, HotelYearTimeSeriesTransformer

import pandas as pd
from src.application.GetHotelsYearsTimeSerie import GetHotelsYearsTimeSerie

df_tripadvisor = Connection().getDataSet('tripadvisor2')
class HotelsRouter(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        
        service = FetchHotels(HotelsDomainService(df_tripadvisor))
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)
        
class PopularityRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        service = FetchHotelsByPopularity(HotelsDomainService(df_tripadvisor),  HotelPopularityTransformer())
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)

class PopularityDistributionRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        args = FilterAdapter().adapt()
        service = FetchHotelsSentimentDistribution(HotelsDomainService(df_tripadvisor), HotelPopularityDistributionTransformer())

        response = service.process(FetchHotelsSentimentDistributionCommand(args))
        
        return Response(0,'ha stato tutto benne!',  response,  200)

class YearTimeSeriesRouter(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        
        service = GetHotelsYearsTimeSerie(HotelsDomainService(df_tripadvisor), HotelYearTimeSeriesTransformer())
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)
class MainRouter:
    def __init__(self,api):
        self.api = api
    
    def init(self):
        self.api.add_resource(HotelsRouter, '/hotels')
        self.api.add_resource(PopularityRouter, '/hotels/popularity')
        self.api.add_resource(PopularityDistributionRouter, '/hotels/popularity/distribution')
        self.api.add_resource(YearTimeSeriesRouter, '/hotels/popularity/distribution/yearTimeSeries')
