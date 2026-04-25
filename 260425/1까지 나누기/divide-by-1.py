n = int(input())
count = 0  # 나눗셈 횟수를 저장할 변수
divisor = 1 # 나눌 수 (1, 2, 3, ...)

while True:
    n = n // divisor # 몫을 다시 n에 저장
    count += 1       # 나눗셈을 했으니 횟수 추가
    
    if n <= 1:       # 몫이 1 이하가 되면 종료
        break
        
    divisor += 1     # 다음에 나눌 수를 1 증가 (2, 3, 4...)

print(count)