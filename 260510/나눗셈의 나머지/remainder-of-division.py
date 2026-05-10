a, b = map(int, input().split())
cnt = [0] * 10
sums = 0

while a > 1:
    cnt[a % b] += 1
    a = a // b

for i in cnt:
    sums += i * i

print(sums)