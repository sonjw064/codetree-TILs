arr = list(map(int,input().split()))
a = sum(arr[::2])
b = sum(arr[1::2])
if a >= b :
    print(a-b)
else :
    print(b-a)
