arr = list(map(int,input().split()))

sums = sum(arr[1::2])
avg = 0
cnt = 0
for i in arr[2::3]:
    avg += i
    cnt += 1
print(f"{sums} {avg / cnt:.1f}")
