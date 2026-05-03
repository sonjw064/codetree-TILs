n = int(input())
arr = []
cnt = 0
for i in range(n):
    num = list(map(int,input().split()))
    if sum(num) / 4 >= 60:
        print("pass")
        cnt += 1
    
    else :
        print("fail")
        
    
print(cnt)


