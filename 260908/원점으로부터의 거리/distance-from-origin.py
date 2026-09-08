n = int(input())
points = []

for i in range(1, n + 1):
    x, y = map(int, input().split())
    dist = abs(x) + abs(y)
    # (거리, 점 번호) 구조로 저장하면 정렬이 매우 쉬워집니다.
    points.append((dist, i))

# 1. 거리 오름차순 -> 2. 번호 오름차순 자동 정렬
points.sort()

for dist, idx in points:
    print(idx)