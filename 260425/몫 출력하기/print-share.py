
count = 0  # 작업 횟수를 셀 변수

while True:
   
    # 1. 종료 조건: 작업을 3번 완료하면 루프 탈출
    if count == 3:
        break
    
    a = int(input())
    
    # 2. 짝수 판별 및 작업 수행
    if a % 2 == 0:
         # 몫을 다시 a에 저장 (핵심!)
        print(a // 2)
        count += 1
    else:
        # 홀수일 때는 아무 작업도 하지 않음 (pass)
        pass
    
   