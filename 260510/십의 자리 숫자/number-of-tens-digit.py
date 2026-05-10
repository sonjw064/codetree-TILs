arr = list(map(int,input().split()))
num = [0] * 10
for i in arr:
    if i == 0:
        break
    num[i // 10] += 1
for j in range(1,10):
    print(f"{j} - {num[j]}")