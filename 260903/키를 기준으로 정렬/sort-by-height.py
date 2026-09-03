class poeple:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
man = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    man.append(poeple(n_i, int(h_i), int(w_i)))

man.sort(key=lambda x: x.height)

for i in man:
    print(i.name, i.height, i.weight)

# Please write your code here.