from src.domain.services.ReviewsService import ReviewsDomainService
class CountReviews:
    def __init__(self, domainService: ReviewsDomainService, transformer):
        self.domainService = domainService  
        self.transformer = transformer
    
    def process(self, command):
        params = command.params()
        startDate = params['startDate'] if 'startDate' in params else None
        endDate = params['endDate'] if 'endDate' in params else None
        
        self.transformer.write(self.domainService.allReviewsCount(startDate, endDate),command.params())
        return self.transformer.read()
    
class CountReviewsCommand:
    def __init__(self, params):
        self.aParams = params
    
    def params(self):
        return self.aParams