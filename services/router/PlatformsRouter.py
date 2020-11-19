import pandas as pd
from flask import Flask
from helpers.FilterAdapter import FilterAdapter
from response import response_resource_fields, Response
from config.client.PyMongoConnectionClient import Connection
from flask_restful import Resource, Api, marshal_with, marshal, reqparse
from src.application.FetchPlatforms import FetchPlatforms
from src.domain.services.PlatformService import PlatformService as PlatformsDomainService

df_tripadvisor = Connection().getDataSet('tripadvisor')
df_tripadvisor = Connection().getMergedDataSet()
class PlatformsRouter(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        
        service = FetchPlatforms(PlatformsDomainService(df_tripadvisor))
        response = service.process()
        
        return Response(0,'è andato tutto benne!',  response,  200)
        
class MainRouter:
    def __init__(self,api):
        self.api = api
    
    def init(self):
        self.api.add_resource(PlatformsRouter, '/platforms')
