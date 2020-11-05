def checkWordsInArray(listA: list, listB: list, strict: bool = False) -> bool:
    if strict:
        return checkIfAllWordsInList(listA, listB)
    else:
        return checkIfAnyWordInList(listA, listB)

def checkIfAllWordsInList(listA: list, listB: list) -> bool:
    for word in listA:
        if not(word in listB):
            return False
    return True

def checkIfAnyWordInList(listA: list, listB: list) -> bool:
    for word in listA:
        if word in listB:
            return True
    return False
