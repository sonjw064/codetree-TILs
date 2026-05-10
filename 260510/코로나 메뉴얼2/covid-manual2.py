# 결과를 저장할 변수 (각 진료소별 인원수)
count_A = 0
count_B = 0
count_C = 0
count_D = 0

# 3명의 정보를 입력받음
for _ in range(3):
    # 입력 예시: "Y 38" -> symptom에는 'Y', temp에는 38.0 저장
    data = input().split()
    symptom = data[0]
    temp = float(data[1])
                    
                        # 조건에 따른 분류
    if symptom == 'Y' and temp >= 37:
        count_A += 1
    elif symptom == 'N' and temp >= 37:
        count_B += 1
    elif symptom == 'Y' and temp < 37:
        count_C += 1
    else: # symptom == 'N' and temp < 37
        count_D += 1

                                                                        # 결과 출력 (A B C D 순서대로)
print(count_A, count_B, count_C, count_D, end="")

                                                                        # 위급상황 판단 (A가 2명 이상일 때)
if count_A >= 2:
    print(" E")
else:
    print("") # 줄바꿈으로 마무리
                                                                                