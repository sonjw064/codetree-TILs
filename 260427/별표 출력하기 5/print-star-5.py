n = int(input())
for i in range(n, 0, -1):      # i = n, n-1, ..., 1 (그룹 수 & 별 개수)
    for j in range(i):          # 그룹 수: i번 반복
        print("*" * i, end=" ") # 별 i개짜리 그룹
    print()