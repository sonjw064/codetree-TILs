n = int(input())
cnt = 0
while True:
    if n == 2**cnt:
        break
    else :
        cnt += 1
print(cnt)