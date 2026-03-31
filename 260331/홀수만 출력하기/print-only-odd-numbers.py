n = int(input())  # 몇 개의 숫자를 입력받을지 n에 저장

for i in range(n):
    num = int(input())  # 입력받은 숫자를 변수 num에 저장
    
    # 입력받은 숫자(num)가 홀수(나머지가 1)인지 확인
    if num % 2 == 1:
        # 홀수라면, 3의 배수(나머지가 0)인지 한 번 더 확인
        if num % 3 == 0:
            print(num)