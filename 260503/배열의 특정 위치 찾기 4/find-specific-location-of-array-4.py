arr = []
cnt = 0
sums = 0
num = map(int,input().split())
for i in num:
    if i == 0:
        break
    if i % 2 == 0:
        arr.append(i)
        cnt += 1
sums = sum(arr)  
print(cnt, sums) 