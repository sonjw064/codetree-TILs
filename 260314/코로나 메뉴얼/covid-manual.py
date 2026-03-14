arr1 = input().split()
arr2 = input().split()
arr3 = input().split()

a1 = arr1[0]
a2 = int(arr1[1])
b1 = arr2[0]
b2 = int(arr2[1])
c1 = arr3[0]
c2 = int(arr3[1])

if a1 == "Y" and a2 >= 37 :
    if (b1 == "Y" and b2 >= 37) or (c1 == "Y" and c2 >= 37):
        print("E")
    else: print("N")

else:  
    if (b1 == "Y" and b2 >= 37) and (c1 == "Y" and c2 >= 37):
        print("E")
    else: print("N")