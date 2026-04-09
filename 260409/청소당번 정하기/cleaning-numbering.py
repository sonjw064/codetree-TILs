n = int(input())
cc = 0
lc = 0
bc = 0

for i in range(1, n+1):
    if i % 12 == 0 :
        bc += 1
    elif i % 3 == 0 :
        lc += 1
    elif i % 2 == 0:
        cc += 1
        
   
    
print(cc, lc, bc)

