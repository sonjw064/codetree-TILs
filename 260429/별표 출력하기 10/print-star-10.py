n = int(input())
up = 0
down = n+1
for i in range(1,n+1):
    if i % 2 == 1:
        up += 1
        print("* " * up)
    else :
        down -= 1
        print("* " * down)
if n % 2 == 1:
    val = 2
     
else: val = 1


    
for i in range(val,n+val):
    if i % 2 == 1:
        print("* " * down)
        down += 1
    else :
        print("* " * up)
        up -= 1