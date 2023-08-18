def isAnagram(s: str, t: str):
    if len(s) == len(t) :
       return sorted(s) == sorted(t)
    else:
      return False
      
  isAnagram('abc','cba')
