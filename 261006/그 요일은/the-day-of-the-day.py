m1, d1, m2, d2 = map(int, input().split())
A = input().strip()

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def to_num(m, d):
    return sum(days[:m - 1]) + d

start = to_num(m1, d1)
end = to_num(m2, d2)

count = 0
for k in range(end - start + 1):
    if names[k % 7] == A:
        count += 1

print(count)