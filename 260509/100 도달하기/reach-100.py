n = int(input())
arr = [1,n]
i = 2
while True:
    val = (arr[i-1] + arr[i-2])
    arr.append(val)
    if val >= 100 :
        break
    i += 1
print(*arr)
