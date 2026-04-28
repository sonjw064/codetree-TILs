n = int(input())

for i in range(1, 2 * n):
    stars = i if i <= n else 2 * n - i
    spaces = n - stars
    print(" " * spaces + "* " * stars)