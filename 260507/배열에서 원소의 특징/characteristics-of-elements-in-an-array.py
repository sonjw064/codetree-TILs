arr = list(map(int, input().split()))

for i in range(len(arr)):
    # 만약 현재 위치(i)의 원소가 3의 배수라면
    if arr[i] % 3 == 0:
        # i가 0이라면 그 앞의 원소가 없으므로, 0보다 클 때만 출력
        if i > 0:
            print(arr[i - 1])
        break # 3의 배수를 찾았으니 멈춤