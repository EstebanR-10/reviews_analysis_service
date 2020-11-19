from flask import Flask, jsonify, send_from_directory
from flask_restful import Resource, Api, marshal_with, marshal, reqparse
from models.Hotel import hotel_resource_fields, Hotel
from config.client.PyMongoConnectionClient import Connection
from src.application.FetchHotels import FetchHotels
from src.application.CountReviews import CountReviews, CountReviewsCommand
from src.domain.services.ReviewsService import ReviewsDomainService
from response import response_resource_fields, Response
from helpers.FilterAdapter import FilterAdapter
from src.application.transformers.ReviewsTransformer import ReviewsCountTransformer, WordFrequencyTrasnformer
from src.application.GetReviewsWordsFrequence import GetReviewsWordsFrequence, Command as GetReviewsWordsFrequenceCommand
from src.application.GetAprioriReviewRules import GetAprioriReviewRules, GetAprioriReviewRulesCommand
from src.application.transformers.AprioriTransformer import AprioriTransformer
from src.domain.services.NaturalLanguageProcessingService import NaturalLanguageProcessingService
from src.application.GetReviewsXmls import GetReviewsXmls
from src.Infrastructure.ReviewsService import ReviewsService as ReviewsInfrService

df_tripadvisor = Connection().getDataSet('tripadvisor')

"""
Endpoint de reviews
"""
class ReviewsRouter(Resource):
    def get(self):
        service = GetReviewsXmls(ReviewsInfrService(df_tripadvisor))
        response = service.process()
        return send_from_directory(response['directory'], response['filename'], as_attachment=True)

"""
Endpoint encargado del conteo de reviews
"""
class ReviewsCountRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        args = FilterAdapter().adapt()
        service = CountReviews(ReviewsDomainService(df_tripadvisor), ReviewsCountTransformer())
        response = service.process(CountReviewsCommand(args))
        
        return Response(0,'è andato tutto benne!',  response,  200)

"""
Endpoint encargado de la obtención de la frecuencia de palabras
"""
class ReviewsWordsFrequencyRouter(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        args = FilterAdapter().adapt()
        service = GetReviewsWordsFrequence(ReviewsDomainService(df_tripadvisor), WordFrequencyTrasnformer())
        response = service.process(GetReviewsWordsFrequenceCommand(args))
        
        return Response(0,'è andato tutto benne!',  response,  200)

"""
Endpoint encargado de la obtención de las reglas de asociación entre las palabras de los documentos
"""
class AprioriReviewRules(Resource):
     @marshal_with(response_resource_fields)
     def get(self):
        args = FilterAdapter().adapt()
        service = GetAprioriReviewRules(NaturalLanguageProcessingService(df_tripadvisor), AprioriTransformer())
        response = service.process(GetAprioriReviewRulesCommand(10, args))
        
        return Response(0,'è andato tutto benne!',  response,  200)

class MainRouter:
    def __init__(self,api):
        self.api = api
    
    def init(self):
        self.api.add_resource(ReviewsRouter, '/reviews')
        self.api.add_resource(ReviewsCountRouter, '/reviews/count')
        self.api.add_resource(ReviewsWordsFrequencyRouter, '/reviews/wordsFrequence')
        self.api.add_resource(AprioriReviewRules, '/reviews/apriori')
