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
from src.application.GetAprioriReviewRules import GetAprioriReviewRules, GetAprioriReviewRulesCommand
from src.application.transformers.AprioriTransformer import AprioriTransformer
from src.domain.services.NaturalLanguageProcessingService import NaturalLanguageProcessingService
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

"""
Endpoint encargado de la obtención de la frecuencia de palabras
"""
class ReviewsWordsFrequencyRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        service = GetReviewsWordsFrequence(ReviewsDomainService(df_tripadvisor), WordFrequencyTrasnformer())
        response = service.process()
        
        return Response(0,'ha stato tutto benne!',  response,  200)

"""
Endpoint encargado de la obtención de las reglas de asociación entre las palabras de los documentos
"""
class AprioriReviewRules(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        args = FilterAdapter().adapt()
        service = GetAprioriReviewRules(NaturalLanguageProcessingService(df_tripadvisor), AprioriTransformer())
        response = service.process(GetAprioriReviewRulesCommand(10, args))
        
        return Response(0,'ha stato tutto benne!',  response,  200)

class MainRouter:
    def __init__(self,api):
        self.api = api
    
    def init(self):
        self.api.add_resource(ReviewsRouter, '/reviews')
        self.api.add_resource(ReviewsCountRouter, '/reviews/count')
        self.api.add_resource(ReviewsWordsFrequencyRouter, '/reviews/wordsFrequence')
        self.api.add_resource(AprioriReviewRules, '/reviews/apriori')
