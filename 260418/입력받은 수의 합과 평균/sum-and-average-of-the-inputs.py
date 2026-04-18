n = int(input())
sums = 0
count = 0
for i in range(1, n+1):
    a = int(input())
    sums += a
    count += 1

if count != 0:
    avg = sums / count
else : avg = 0.0
print(f"{sums} {avg:.1f}")

