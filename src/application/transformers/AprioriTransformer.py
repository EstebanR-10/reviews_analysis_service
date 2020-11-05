from helpers.Tools import checkWordsInArray

class AprioriTransformer:
    __data = {}
    
    def write(self, rules: list, size: int = 20, words: str = None, strict: bool=False):
        self.generateAssociationRulesGraphData(rules, size, words, strict)

    def generateAssociationRulesGraphData(self, association_rules: list, size: int, words: str = None, strict: bool=False):
        my_set=set()
        links = []
        not_duplicade_links = []
        rules = []

        if words:
            association_rules_by_specific_words = []
            for rule in association_rules:
                pair = rule[0] 
                items = [x for x in pair]
                if checkWordsInArray(words, items, strict):
                    association_rules_by_specific_words.append(rule)
            association_rules = association_rules_by_specific_words

        for rule in association_rules[:size]:
            #Construccion del set de las palabras participantes en las reglas
            my_set = my_set.union(rule[0])

            #construccion de las reglas en el formato indicado
            pair = rule[0] 
            items = [x for x in pair]
            for i in range(0,len(items)-1):
                links.append((items[i], items[i+1]))
            rules.append({ 'items':items, 'support':rule[1], 'confidence':rule[2][0][2] })

        links = set(links)
        for link in links:
            not_duplicade_links.append({'source': link[0], 'target': link[1]})

        nodes = [{'id': word, 'color': 'black'} for word in my_set]

        self.__data['rules'] = rules
        self.__data['adjacencyList'] = { 'nodes': nodes, 'links': not_duplicade_links }
        self.__data['numberOfRules'] =  size if len(association_rules) >= size else len(association_rules)
        self.__data['rulesTotalCount'] = len(association_rules)
        
    def read(self) -> dict:
        return self.__data