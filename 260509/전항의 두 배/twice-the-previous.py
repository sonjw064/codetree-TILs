a1, a2 = map(int,input().split())
arr = []
arr.append(a1)
arr.append(a2)

for i in range(2,10):
    val = (arr[i-1] + (2 * arr[i-2]))
    arr.append(val)
print(*arr)


