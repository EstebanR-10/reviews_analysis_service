from flask_restful import reqparse
from flask_restful import fields
import re



class FilterAdapter:
    __allowed_params = {}
    __aParser = reqparse.RequestParser()
   
    
    def __init__(self):
        self.__allowed_params['sent'] = [0,1,2]
        self.__aParser.add_argument('sent', type=str, help='label representing the sentiment of a value')

    def adapt(self):
        params = self.__aParser.parse_args()
        for param in params:
            if params[param] != None:
                self.__allowed_params[param] =  self.parseSentimentParam(params['sent'])
                return self.__allowed_params
        return self.__allowed_params

    def parser(self):
        return self.__aParser

    def parseSentimentParam(self, string):
        sents = re.findall(r'[0-2]', string)
        return [int(sent) for sent in sents]