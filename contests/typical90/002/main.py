from itertools import product

def isvalid(S):
    chars = ''.join(S)
    while '()' in chars:
        chars = chars.replace('()', '')
    
    return chars == ""


N = int(input())
for S in product(['(', ')'], repeat=N):
    if isvalid(S):
        print(*S, sep='')
