a, b, c, d = map(int, input().split())
count = 0
while True:
    if a == c and b == d:
        break

    count += 1
    b += 1

    if b == 60:
        a += 1
        b = 0

print(count)