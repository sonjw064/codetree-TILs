n = int(input())

def sums(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s // 10
print(sums(n))