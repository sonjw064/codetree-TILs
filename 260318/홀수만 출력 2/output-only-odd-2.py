B, A = map(int,input().split())

if B % 2 == 1:
    for i in range(B, A-1, -2):
        print(i, end= " ")