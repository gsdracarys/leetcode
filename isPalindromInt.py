def isPalindrome( x: int) -> bool:
    strx = len(str(x))
    if str(x) == str(x)[::-1]:
            return True
    else:
        return False

print(isPalindrome(1221))