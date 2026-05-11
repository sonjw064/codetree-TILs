
chars = ['L', 'E', 'B', 'R', 'O', 'S']


target = input().strip()


if target in chars:
    print(chars.index(target))
else:
    print("None")
