check = True
for i in range(1,6):
    n = int(input())
    if n % 3 != 0:
        check = False
if check == True:
    print("1")
else :
    print("0")