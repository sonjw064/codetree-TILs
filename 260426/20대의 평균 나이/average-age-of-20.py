cnt = 0
sum = 0
while True:
    age = int(input())
    if age > 29 :
        break
    sum += age
    cnt += 1
   
    
val = sum / cnt

print(f"{val:.2f}") 