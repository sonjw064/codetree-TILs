a, b = map(int, input().split())

def number3(n):
    s = str(n)
    if ('3' in s) or ('6' in s) or ('9' in s) or (n % 3 == 0):
        return n
def check(a,b):
    cnt = 0
    for n in range(a,b+1):
        if number3(n):
            cnt += 1
    return cnt
print(check(a,b))
        