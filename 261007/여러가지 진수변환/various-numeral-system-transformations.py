N, B = map(int, input().split())

def alter(n,b):
    arr = []
    while True:
        if n < b:
            arr.append(n)
            break
        arr.append(n % b)
        n //= b
        
    return arr[::-1]

for i in alter(N,B):
    print(i,end="")