num = list(map(int,input().split()))
arr = [0] * 7
for i in num:
    arr[i] += 1
for i in range(1,7):
    print(f"{i} - {arr[i]}")  


