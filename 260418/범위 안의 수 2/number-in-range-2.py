# 1. 입력을 리스트로 변환 (순회하기 편하게 함)
numbers = list(map(int, input().split()))

sums = 0
count = 0

# 2. 리스트의 각 요소를 직접 확인
for val in numbers:
    # 조건: 0 이상 200 이하
    if 0 <= val <= 200:
        sums += val
        count += 1

# 3. 평균 계산 (0으로 나누는 에러 방지 포함)
if count > 0:
    avg = sums / count
else:
    avg = 0.0

# 4. 결과 출력
print(f"{sums} {avg:.1f}")

