# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, K):
    # write your code in Python 2.7
    
    n = len(S)
    S = list(S)
    
    if n <= K:
        for i in reversed(range(n)):
            if ord(S[i]) >= 97 and ord(S[i]) <= 122:
                S[i] = chr(ord(S[i]) - 32)
            elif S[i] == "-" and i != 0:
                S[i] = S[i-1]
                S[i-1] = "-"
        for i in range(n):
            if S[i] != "-":
                break
        return "".join(S[i:])
        
    i = n-1
    kay = 0
    while i >= 0:
        if kay == K:
            temp = S[i]
            S[i] = "-"
        if kay > K:
            temp2 = S[i]
            S[i] = temp
            temp = temp2
        if S[i] == "-":
            if kay < K and i != 0:
                S[i] = S[i-1]
                S[i-1] = "-"
            elif kay > K:
                S[i] = temp
                kay = kay - K - 1  
        if ord(S[i]) >= 97 and ord(S[i]) <= 122:
            S[i] = chr(ord(S[i]) - 32)  
        i = i - 1
        kay = kay + 1
        
            
    for i in range(n):
        if S[i] != "-":
            break
    return "".join(S[i:])        
            
            