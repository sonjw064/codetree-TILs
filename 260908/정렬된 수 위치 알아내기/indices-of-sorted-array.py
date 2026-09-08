n = int(input())
sequence = list(map(int, input().split()))

q = []
for i in range(n):
    q.append((sequence[i],i))

q.sort()

ans = [0] * n

for rank, (num, original_idx) in enumerate(q, start=1):
    ans[original_idx] = rank

print(*ans)