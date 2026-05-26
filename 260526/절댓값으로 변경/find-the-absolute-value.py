n = int(input())
arr = list(map(int, input().split()))

def wjf(lists):
    for i in range(len(lists)):
        if lists[i] < 0:
            lists[i] = lists[i] * -1
        
wjf(arr)
print(*arr)
