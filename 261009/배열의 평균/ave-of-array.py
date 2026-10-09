arr1 = []
for i in range(2):
    arr2 = list(map(int,input().split()))
    arr1.append(arr2)

def x(a):
    sums = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            sums += a[i][j]
        ave = sums / len(a[0])
        print(f"{ave:.1f}", end=" ")
        sums = 0
        ave = 0

#00 01 10 11 20 21  
def y(a):
    sums = 0
    for i in range(len(a[0])):
        for j in range(len(a)):
            sums += (a[j][i])
        ave = sums / len(a)
        print(f"{ave:.1f}",end=" ")
        sums = 0
        ave = 0
     
def z(a):
    sums = 0
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            sums += a[i][j]
            cnt += 1
    ave = sums / cnt
    print(f"{ave:.1f}")

x(arr1)
print()
y(arr1)
print()
z(arr1)
