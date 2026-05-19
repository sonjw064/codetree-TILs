
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_lcm(n, m):
   return (n * m) // get_gcd(n, m)

n, m = map(int, input().split())

print(get_lcm(n, m))