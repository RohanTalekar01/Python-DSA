from string import ascii_lowercase
from string import ascii_uppercase
def checkPangram(s):

    for ch in ascii_lowercase and ascii_uppercase:
        if ch not in s:
            return False
        return True

s= "The quick brown fox jumps Over the LAZY dog"

print(checkPangram(s))
