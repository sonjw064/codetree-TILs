arr = []
cnt = 0
sums = 0
num = map(int,input().split())
for i in num:
    if i == 0:
        break
    arr.append(i)
    cnt += 1
sums = sum(arr)
arg = sums / cnt
print(f"{sums} {arg:.1f}")
   
