import re
from datetime import datetime
from flask_restful import reqparse, fields, inputs



class FilterAdapter:
    __ALLOWED_PARAMS = {'sent': 'sent', 'words':'words', 'strict':'strict', 'hotels':'hotels', 'startDate':'startDate', 'endDate':'endDate'}
    __params_received = {}
    __aParser = reqparse.RequestParser()
   
    
    def __init__(self):
        self.__params_received = {}
        self.__params_received['sent'] = [0,1,2]
        self.__aParser.add_argument('sent', type=str, help='label representing the sentiment of a value')
        self.__aParser.add_argument('support', type=float, help='level of support for apriori algorithm')
        self.__aParser.add_argument('confidence', type=float, help='level of confidence for apriori algorithm')
        self.__aParser.add_argument('words', type=str, help='list of words of for including in apriori algorithm')
        self.__aParser.add_argument('takeRules', type=int, help='number of rules to return')
        self.__aParser.add_argument('strict', type=inputs.boolean, help='boolean that defines if all words should be taked')
        self.__aParser.add_argument('hotels', type=str, help='hotels to be displayed')
        self.__aParser.add_argument('startDate', type=inputs.date, help='fecha inicial para filtrar entre periodos')
        self.__aParser.add_argument('endDate', type=inputs.date, help='fecha de fin para filtrar entre periodos')

    def adapt(self):
        params = self.__aParser.parse_args()
        for param in params:
            if params[param] != None:
                self.__params_received[param] = self.parseParams(param)(params[param])
        return self.__params_received

    def parser(self):
        return self.__aParser

    def parseParams(self, param: str):
        if param == self.__ALLOWED_PARAMS['sent']:
            return self.parseSentimentParam
        elif param == self.__ALLOWED_PARAMS['words'] or param == self.__ALLOWED_PARAMS['hotels']:
            return self.parseWords
        else:
            return lambda x: x

    def parseSentimentParam(self, string: str) -> list:
        sents = re.findall(r'[0-2]', string)
        return [int(sent) for sent in sents]
    
    def parseWords(self, string: str) -> list:
        return re.split(',', string)

    """ Desactivada temporalmente
    def parseDateRange(self, startDate: datetime, endDate: datetime) -> list:
        return [startDate,endDate]
    """