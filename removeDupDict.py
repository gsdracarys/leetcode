# Given the above dict sort and remove duplicates
def removeDupDict(adict: dict) -> dict:
    fDict = {}
    for k,v in adict.items():
        print(adict.get(k))

if __name__ == "__main__":
    mydict = {'apple': 2, 'red': 3, 'pear': 1}