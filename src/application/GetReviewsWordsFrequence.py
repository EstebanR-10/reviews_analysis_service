from src.application.transformers.ReviewsTransformer import WordFrequencyTrasnformer
from src.domain.services.ReviewsService import ReviewsDomainService

class GetReviewsWordsFrequence:

    def __init__(self, domainService: ReviewsDomainService, transformer: WordFrequencyTrasnformer):
        self.domainService = domainService
        self.transformer = transformer

    def process(self, command):
        params = command.params()
        startDate = params['startDate'] if 'startDate' in params else None
        endDate = params['endDate'] if 'endDate' in params else None

        df = self.domainService.wordsFrequency(startDate, endDate)
        self.transformer.write(df)
        return self.transformer.read()

class Command:

    def __init__(self, params):
        self.aParams = params
    
    def params(self):
        return self.aParams