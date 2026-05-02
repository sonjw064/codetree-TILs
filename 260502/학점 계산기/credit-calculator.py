n = int(input())
arr = list(map(float,input().split()))
sums = sum(arr)
arg = sums / n
print(f"{arg:.1f}")
if arg >= 4.0:
    print("Perfect")
elif arg >= 3.0:
    print("Good")
else :
    print("Poor")