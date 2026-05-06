n = int(input())
arr = list(map(int,input().split()))
num = []
for i in arr:
   if i % 2 == 0:
        num.append(i)
print(*num[::-1])
