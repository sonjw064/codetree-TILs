n = int(input())
ch = ord("A")
for i in range(n):
    for j in range(n):
        print(chr(ch+i+j),end="")
    ch += n-1

    print()