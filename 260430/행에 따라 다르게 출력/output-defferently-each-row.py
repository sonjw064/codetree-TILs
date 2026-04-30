N = int(input())

current = 1  # 현재 숫자

for i in range(1, N + 1):
    row = []
    if i % 2 == 1:  # 홀수 번째 줄: 1씩 증가
        for j in range(N):
            row.append(current + j)
        current = row[-1] + 2  # 다음 줄 시작값 = 마지막값 + 2
    else:           # 짝수 번째 줄: 2씩 증가
        for j in range(N):
            row.append(current + j * 2)
        current = row[-1] + 1  # 다음 줄 시작값 = 마지막값 + 2

    print(*row)