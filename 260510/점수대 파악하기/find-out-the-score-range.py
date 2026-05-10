arr = list(map(int,input().split()))
num = [0] * 11
for i in arr:
    if i == 0:
        break
    num[i // 10] += 1
for j in range(10,0,-1):
    print(f"{(j)*10} - {num[j]}")