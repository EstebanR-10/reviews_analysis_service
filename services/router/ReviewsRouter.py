from flask import Flask
from flask_restful import Resource, Api, marshal_with, marshal, reqparse
from models.Hotel import hotel_resource_fields, Hotel
from config.client.PyMongoConnectionClient import Connection
from src.application.FetchHotels import FetchHotels
from src.application.CountReviews import CountReviews
from src.domain.services.ReviewsService import ReviewsDomainService
from response import response_resource_fields, Response
from helpers.FilterAdapter import FilterAdapter

df_tripadvisor = Connection().getDataSet('tripadvisor')
#df_tripadvisor = df_tripadvisor.drop([11890,11891])
sentiment = [0 if int(i)<=20 else 1 if int(i)==30 else 2 for i in df_tripadvisor.rating]
df_tripadvisor['sentiment_label'] = sentiment

"""
Endpoint de reviews
"""
class ReviewsRouter(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        return Response(0,'ha stato tutto benne!',  [],  200)

"""
Endpoint encargado del conteo de reviews
"""
class ReviewsCountRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        args = FilterAdapter().adapt()
        service = CountReviews(ReviewsDomainService(df_tripadvisor))
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)

class MainRouter:
    def __init__(self,api):
        self.api = api
    
    def init(self):
        self.api.add_resource(ReviewsRouter, '/reviews')
        self.api.add_resource(ReviewsCountRouter, '/reviews/count')
