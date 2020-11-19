class PlatformService:
    def __init__(self, df):
        self.df = df

    def allPlatformsList(self):
        return self.df.platform.unique().tolist()