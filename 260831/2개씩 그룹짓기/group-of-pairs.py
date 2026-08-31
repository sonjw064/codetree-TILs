n = int(input())
nums = list(map(int, input().split()))

nums.sort()
max = 0
for i in range(n) :
    val = (nums[i]+nums[2*n -1 - i])
    if max < val :
        max = val
print(max)
# Please write your code here.
