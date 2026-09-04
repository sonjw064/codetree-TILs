class per:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

n = int(input())
p = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    p.append(per(n_i, int(h_i), int(w_i)))

p.sort(key= lambda x : (x.h, -x.w))

for i in p:
    print(i.n, i.h, i.w)

# Please write your code here.