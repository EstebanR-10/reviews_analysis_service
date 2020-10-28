from flask import Flask
from flask_restful import Resource, Api, marshal_with, marshal, reqparse
from models.Hotel import hotel_resource_fields, Hotel
from config.client.PyMongoConnectionClient import Connection
from src.application.FetchHotels import FetchHotels
from src.application.CountReviews import CountReviews, CountReviewsCommand
from src.domain.services.ReviewsService import ReviewsDomainService
from response import response_resource_fields, Response
from helpers.FilterAdapter import FilterAdapter
from src.application.transformers.ReviewsTransformer import ReviewsCountTransformer, WordFrequencyTrasnformer
from src.application.GetReviewsWordsFrequence import GetReviewsWordsFrequence

df_tripadvisor = Connection().getDataSet('tripadvisor')

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
        service = CountReviews(ReviewsDomainService(df_tripadvisor), ReviewsCountTransformer())
        response = service.process(CountReviewsCommand(args))
        
        return Response(0,'ha stato tutto benne!',  response,  200)

class ReviewsWordsFrequencyRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        service = GetReviewsWordsFrequence(ReviewsDomainService(df_tripadvisor), WordFrequencyTrasnformer())
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)

class MainRouter:
    def __init__(self,api):
        self.api = api
    
    def init(self):
        self.api.add_resource(ReviewsRouter, '/reviews')
        self.api.add_resource(ReviewsCountRouter, '/reviews/count')
        self.api.add_resource(ReviewsWordsFrequencyRouter, '/reviews/wordsFrequence')
