# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

sum_val = 0
    
# Case 1. b가 더 큰 경우 
if a <= b:
    for i in range(a, b + 1):
        if i % 5 == 0:
            sum_val += i

# Case 2. a가 더 큰 경우
else:
    for i in range(b, a + 1):
        if i % 5 == 0:
            sum_val += i

print(sum_val)
