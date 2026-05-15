from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

counts = Counter(nums)
unique_nums = [num for num, count in counts.items() if count == 1]

if unique_nums:
    print(max(unique_nums))
else:
    print(-1)  
