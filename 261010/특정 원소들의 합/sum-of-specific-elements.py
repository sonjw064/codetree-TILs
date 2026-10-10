arr1 = []
a = 1
sums = 0
for i in range(4):
       arr2 = list(map(int,input().split()))
       arr1.append(arr2)
if a < 4:       
    for i in range(4):
        for j in range(a):
            sums += arr1[i][j]
        a += 1
    a = 1
print(sums) 

