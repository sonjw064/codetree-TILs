# 1. 정수 N 입력받기
n = int(input())

# 2. 약수들의 합을 저장할 변수 초기화
divisor_sum = 0

# 3. 1부터 n-1까지 돌면서 약수 찾기
# (자기 자신은 제외해야 하므로 n 미만까지 반복)
for i in range(1, n):
    if n % i == 0:        # n을 i로 나눴을 때 나머지가 0이면 약수!
        divisor_sum += i  # 약수를 합계에 더함

# 4. 결과 판단 및 출력
if divisor_sum == n:
    print("P")
else:
    print("N")