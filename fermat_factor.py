import sys
import math

n = int(sys.argv[1])
m = int(math.sqrt(n)) + 1
s_sqr = 0

for i in range(m, n):
    s_sqr = i ** 2 - n
    print(f"s^2: {s_sqr}, s: {math.sqrt(s_sqr)}, i: {i}, i^2: {i**2}")
    if math.sqrt(s_sqr).is_integer():
        break

s = int(math.sqrt(s_sqr))
print(f"divisors: {i - s}, {i + s}")
