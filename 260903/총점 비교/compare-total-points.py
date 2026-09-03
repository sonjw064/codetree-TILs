class scr:
    def __init__(self, name, scr1, scr2, scr3):
        self.name = name
        self.scr1 = scr1
        self.scr2 = scr2
        self.scr3 = scr3



n = int(input())
h = []

for _ in range(n):
    name, scr1, scr2, scr3 = input().split()
    h.append(scr(name, int(scr1), int(scr2), int(scr3)))

h.sort(key= lambda x: (x.scr1 + x.scr2 + x.scr3))

for i in h:
    print(i.name, i.scr1, i.scr2, i.scr3)


# Please write your code here.