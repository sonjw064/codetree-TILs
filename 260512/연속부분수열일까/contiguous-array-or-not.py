a, b = map(int,input().split())
a1 = list(map(int,input().split()))
b1 = list(map(int,input().split()))

check = False
for i in range((a - b)+1):
    if a1[i:i+b] == b1:
        check = True

if check:
    print("Yes")
else:
    print("No")

