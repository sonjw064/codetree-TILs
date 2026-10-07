N = list(map(int,input()))


#2진수를 10진수로 변환
def two():
    non = 0
    for i in range(len(N)):
        non = non * 2 + N[i]
    return  non * 17
  
#*17

#10진수를 2진수로 변환

def ten(n):
    arr = []
    while True:
        if n < 2:
            arr.append(n)
            break
        
        arr.append(n % 2)
        n //= 2

    return arr[::-1]

for i in ten(two()):
    print(i,end="")

