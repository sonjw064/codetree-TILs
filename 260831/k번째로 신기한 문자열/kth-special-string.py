n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

word = [i for i in str if i.startswith(t)]
word.sort()
print(word[k-1])