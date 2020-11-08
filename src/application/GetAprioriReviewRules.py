from src.application.transformers.AprioriTransformer import AprioriTransformer 
from src.domain.services.NaturalLanguageProcessingService import NaturalLanguageProcessingService

class GetAprioriReviewRules:

    def __init__(self, domainService: NaturalLanguageProcessingService, transformer: AprioriTransformer):
        self.domainService = domainService
        self.transformer = transformer

    def process(self, command):
        params = command.params()
        takeRules = params['takeRules'] if 'takeRules' in params else 20
        words = params['words'] if 'words' in params else None
        strict = params['strict'] if 'strict' in params else False

        rules = self.domainService.apriori(command.wordsQuantity(), params)
        self.transformer.write(rules, takeRules, words, strict )
        return self.transformer.read()

class GetAprioriReviewRulesCommand:
    def __init__(self, wordsQuantity=10, params: dict = {}):
        self.aWordsQuantity = wordsQuantity
        self.aParams = params

    def wordsQuantity(self):
        return self.aWordsQuantity
    
    def params(self):
        return self.aParams