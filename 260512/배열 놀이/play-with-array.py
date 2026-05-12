n, q = map(int,input().split())
n_list = list(map(int,input().split()))
for i in range(q):
    check = list(map(int,input().split()))
    if check[0] == 1:
       print(n_list[check[1]-1])
    elif check[0] == 2:
        if check[1] in n_list:
            print((n_list.index(check[1]))+1)
        else:
            print("0")
    elif check[0] == 3:
        print(*n_list[check[1]-1:check[2]])
