cnt = 0
sum = 0

while True:
    age = int(input())
    if 20 <= age <= 29 :
        sum += age
        cnt += 1
    else : break
val = sum / cnt
print(f"{val:.2f}") 