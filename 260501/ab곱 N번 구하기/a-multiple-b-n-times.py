n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    sums = 1
    for j in range(a, b+1):
        sums *= j
    print(sums)
    