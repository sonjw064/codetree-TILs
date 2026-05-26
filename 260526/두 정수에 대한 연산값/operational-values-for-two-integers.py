a, b = map(int, input().split())

def sums(a,b):
    if a > b:
        return (a + 25),(b * 2)
    else:
        return (a * 2),(b + 25)

x, y = sums(a,b)
print(x,y)
