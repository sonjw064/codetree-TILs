n = int(input())
arr = list(map(int, input().split()))
val = []
for i in range(n):
    if i % 2 == 0 :
        sorted_arr = sorted(arr[: i+1])

        median = sorted_arr[len(sorted_arr) // 2]

        print(median, end=" ")

     

# Please write your code here.