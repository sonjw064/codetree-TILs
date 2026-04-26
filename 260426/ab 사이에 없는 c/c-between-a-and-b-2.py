a , b, c = map(int,input().split())
check = True
for i in range(a, b+1):
    if i % c == 0:
        check = False
if check == True:
    print("YES")
else:
    print("NO")