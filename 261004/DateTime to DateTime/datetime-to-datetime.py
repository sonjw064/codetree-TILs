a, b, c = map(int, input().split())

d = 11
h = 11
m = 11
counts = 0

while True:
    if d == a and h == b and m == c:
        break
    
    # 14일 23시 59분을 넘어가거나 잘못된 입력 방지를 위한 안전 장치
    if d > a or (d == a and h > b) or (d == a and h == b and m > c):
        counts = -1
        break

    counts += 1
    m += 1
    
    if m == 60:
        h += 1
        m = 0
        
    if h == 24:
        d += 1
        h = 0

print(counts)