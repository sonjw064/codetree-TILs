n, m = map(int, input().split())

arr = [[0 for i in range(m)] for j in range(n)]

k = 0
for j in range(m):  # 열을 기준으로 반복
    if j % 2 == 0:  # 짝수 번째 열: 위 -> 아래
        for i in range(n):
            arr[i][j] = k
            k += 1
    else:  # 홀수 번째 열: 아래 -> 위
        for i in range(n - 1, -1, -1):
            arr[i][j] = k
            k += 1
    
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
