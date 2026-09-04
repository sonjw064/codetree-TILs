class p:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = 5
per = []

for _ in range(n):
    n, h, w = input().split()
    per.append(p(n, int(h), float(w)))

per.sort(key= lambda x : (x.name))

print("name")
for i in per:
    print(f"{i.name} {i.height} {i.weight:.1f}")
print("")

per.sort(key= lambda x : (-x.height))
print("height")
for i in per:
   print(f"{i.name} {i.height} {i.weight:.1f}")

# Please write your code here.