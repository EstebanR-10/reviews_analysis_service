from flask_restful import reqparse
from flask_restful import fields
import re

allowed_params = { 'sent': [0,1,2] }

class FilterAdapter:
    aParser = reqparse.RequestParser()
    aParser.add_argument('sent', type=str, help='label representing the sentiment of a value')
    
    def __init__(self):
        print('c')

    def adapt(self):
        params = self.aParser.parse_args()
        for param in params:
            if params[param] != None:
                allowed_params[param] =  self.parseSentimentParam(params['sent'])
                return allowed_params
        return allowed_params

    def parser(self):
        return self.aParser

    def parseSentimentParam(self, string):
        sents = re.findall(r'[0-2]', string)
        return [int(sent) for sent in sents]