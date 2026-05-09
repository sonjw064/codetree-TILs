n = int(input())
arr = [0] * 10
cnt_arr = list(map(int,input().split()))

for i in cnt_arr:
    arr[i] += 1

for i in range(1,10):
    print(arr[i])

