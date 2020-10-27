class CountReviews:
    def __init__(self, domainService, transformer):
        self.domainService = domainService  
        self.transformer = transformer
    
    def process(self, command):
        self.transformer.write(self.domainService.allReviewsCount(),command.filters())
        return self.transformer.read()
    
class CountReviewsCommand:
    def __init__(self, params):
        self.params = params
    
    def filters(self):
        return self.params