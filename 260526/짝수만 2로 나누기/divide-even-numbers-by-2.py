n = int(input())
arr = list(map(int, input().split()))

def dobul(lists):
    for i in range(len(lists)):
        if lists[i] % 2 == 0:
            lists[i] = lists[i] // 2
dobul(arr)
print(*arr)
