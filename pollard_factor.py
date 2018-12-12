import sys
import math

n = int(sys.argv[1])


def recur(num):
    return (num**2 + 1) % n


a = 2
b = 2
step = 0

print(f"n={n}")
while True:
    a = recur(a)
    b = recur(recur(b))
    d = math.gcd(b - a, n)
    print(f"{step}. a: {a}, b: {b}, gcd: {d}\n")
    if 1 < d < n:
        print(d)
        break
    step += 1
