# 변수 선언, 입력
sum_val = 0
cnt = 0

for _ in range(10):
	num = int(input())
	if num >= 0 and num <= 200:
		sum_val += num
		cnt += 1

# 0이상 200이하의 정수들의 평균을 구합니다.
avg = sum_val / cnt

# 출력
print(f"{sum_val} {avg:.1f}")
