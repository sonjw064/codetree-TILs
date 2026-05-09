n = int(input())
cnt = 0
a = 0
arr = []
while True:
    a += n
    arr.append(a)
    if a % 5 == 0:
        cnt += 1
    if cnt == 2:
        break
print(*arr)
    