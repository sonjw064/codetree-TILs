arr = []
i = -1
n = list(map(int,input().split()))
while True:

    i += 1
    if n[i] == 0:
        break
    if n[i] % 2 == 1:
        arr.append(n[i] + 3)
    else :
        arr.append(n[i] // 2)
print(*arr)
