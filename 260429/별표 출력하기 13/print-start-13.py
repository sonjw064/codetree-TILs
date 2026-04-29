n = int(input())
down = n
up = 0
for i in range(1,n+1):
    if i % 2 == 1:
        print("* " * down)
        down -= 1
    else :
        up += 1
        print("* " * up)
if n % 2 == 1:
    val = 2
else :
    val = 1
for i in range(val,n+val):
    if i % 2 == 0:
        down += 1
        print("* " * down)
    else : 
        print("* " * up)
        up -= 1

        
