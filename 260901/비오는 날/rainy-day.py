class weather:
    def __init__(self, date, day, wea):
        self.date = date
        self.day = day
        self.wea = wea


n = int(input())
w = []

for _ in range(n):
    date, day, wea = input().split()
    w.append(weather(date, day, wea))

h = []

for i in w:
    if i.wea == "Rain" :
        h.append(i)

f = h[0]
for j in h:
    if f.date > j.date:
        f = j

print(f.date, f.day, f.wea)



# Please write your code here.