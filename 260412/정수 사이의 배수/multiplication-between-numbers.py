a, b  = map(int,input().split())
sums = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0 :
        sums += i 
        cnt += 1

ave = sums / cnt 

print(f"{sums} {ave:.1f}")
