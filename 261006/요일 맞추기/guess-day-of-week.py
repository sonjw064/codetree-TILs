m1, d1, m2, d2 = map(int, input().split())
days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_year(m, d):
    return sum(month[:m]) + d

diff = day_of_year(m2, d2) - day_of_year(m1, d1)
print(days[(diff + 1) % 7])   # 기존 코드의 counta와 같은 기준