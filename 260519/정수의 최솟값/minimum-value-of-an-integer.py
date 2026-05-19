a, b, c = map(int, input().split())

def add(*args):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else : 
        return c

print(add(a,b,c))