A, B, C = map(int,input().split())

if A < B and A < C :
    if B < C :
        print(B)
    else: print(C)
else :
    if (B < C) and (A < C):
        print(A)
    elif (C < B) and (A < B):
        print(A)
