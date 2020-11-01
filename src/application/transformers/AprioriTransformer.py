class AprioriTransformer:
    __data = {}
    
    def write(self, rules: list, size: int):
        self.generateAssociationRulesGraphData(rules, size)

    def generateAssociationRulesGraphData(self, association_rules: list, size: int):
        my_set=set()
        links = []
        for rule in association_rules[:size]:
            #Construccion del set de las palabras participantes en las reglas
            my_set = my_set.union(rule[0])

            #construccion de las reglas en el formato indicado
            pair = rule[0] 
            items = [x for x in pair]
            for i in range(0,len(items)-1):
                links.append({'source': items[i], 'target': items[i+1]})

        nodes = [{'id': word} for word in my_set]

        self.__data['nodes'] = nodes
        self.__data['links'] = links
        
    def read(self) -> dict:
        return self.__data