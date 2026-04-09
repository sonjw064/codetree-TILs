cnt1 = 0
cnt2 = 0

for _ in range(1, 11):
    a = int(input())

    if a % 3 == 0:
        cnt1 += 1

    if a % 5 == 0:
        cnt2 += 1
print(cnt1, cnt2)