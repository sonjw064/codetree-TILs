n = int(input())
sums = 0
for i in range(1,101):
    sums += i
    if sums >= n :
        break
print(i)
