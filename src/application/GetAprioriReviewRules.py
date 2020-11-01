from src.application.transformers.AprioriTransformer import AprioriTransformer

class GetAprioriReviewRules:

    def __init__(self, domainService, transformer: AprioriTransformer):
        self.domainService = domainService
        self.transformer = transformer

    def process(self):
        rules = self.domainService.apriori(10)
        self.transformer.write(rules, 20)
        return self.transformer.read()