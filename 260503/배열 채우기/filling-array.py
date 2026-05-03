number = []
input_data = map(int,input().split())
for i in input_data:
    num = i
    if num == 0:
        break
    number.append(num)
    if len(number) == 10:
        break
for j in number[::-1]:
    print(j,end=" ")