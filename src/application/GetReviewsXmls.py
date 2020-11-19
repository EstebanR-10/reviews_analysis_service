class GetReviewsXmls:
    def __init__(self, infrastructureService):
        self.service = infrastructureService
    
    def process(self):
        return self.service.allReviewsXmls()