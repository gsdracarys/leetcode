# 1. Convert a list to a dictionary with key as the item and value as the count of the item
def listToDict(alist: list) -> dict:
    adict = {}
    for i in alist:
        if i in adict:
            adict[i] += 1
        else:
            adict[i] = 1

    return adict






print(listToDict([1,2,3,2,3,2]))