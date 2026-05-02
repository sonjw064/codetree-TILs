arr = list(map(int,input().split()))
sums = 0
cnt = 0

for i in arr:
    if i < 250 :
        sums += i
        cnt += 1
    else : break

avl = sums / cnt
print(f"{sums} {avl:.1f}")
