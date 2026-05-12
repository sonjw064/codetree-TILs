n = int(input())
a = list(map(int, input().split()))

mins = min(a)
cnt = a.count(mins)
print(mins,cnt)
