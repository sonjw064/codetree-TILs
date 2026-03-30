n = int(input())

while n <= 100 :
    if n < 60 :
        print("F", end=" ")
    elif n >= 90:
        print("A", end=" ")
    elif n >= 80:
        print("B",end =" ")
    elif n >= 70:
        print("C", end =" ")
    elif n >= 60:
        print("D", end =" ")
    n += 1