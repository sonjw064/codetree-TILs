Am, Ae = map(int,input().split())
Bm, Be = map(int,input().split())

if Am > Bm :
    print("A")
elif Bm > Am :
    print("B")
elif Ae > Be :
    print("A")
elif Be > Ae :
    print("B")