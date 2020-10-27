class GetReviewsWordsFrequence:

    def __init__(self, domainService, transformer):
        self.domainService = domainService
        self.transformer = transformer

    def process(self):
        df = self.domainService.wordsFrequency()
        self.transformer.write(df)
        return self.transformer.read()