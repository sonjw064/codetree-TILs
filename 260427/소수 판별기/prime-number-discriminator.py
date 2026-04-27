
n = int(input())
check = True

for i in range(2, n):
    if i % n == 0:
         check = False
        
        
if check == False:
    print("C")
else : 
    print("P")

