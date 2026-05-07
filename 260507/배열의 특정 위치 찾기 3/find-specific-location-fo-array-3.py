# 1. 한 줄을 입력받아 공백으로 쪼개고 숫자 리스트로 변환
all_input = input().split() 

arr = []
for x in all_input:
    num = int(x) # 이제 x는 "1", "2" 같은 하나하나의 문자열이라 int 변환 가능!
    if num == 0:
        break
    arr.append(num)

# 결과 출력
if len(arr) >= 3:
    print(arr[-1] + arr[-2] + arr[-3])