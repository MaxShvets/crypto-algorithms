import sys
import math


def gen_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gen_gcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inverse(a, modulo):
    g, x, y = gen_gcd(a, modulo)
    if g != 1:
        return None
    else:
        return x % modulo


def mod_pow(n, p, modulo):
    if p < 0:
        n = mod_inverse(n, modulo)
        p = abs(p)

    return n**p % modulo


def print_table_row(values, cell_width):
    for value in values:
        print(f"{value:{cell_width}}|", end="")
    print()


def print_table_separator(cell_amount, cell_width):
    print("+".join(["-" * cell_width] * cell_amount) + "+")


def output_pairs_table(pairs, cell_width):
    print_table_row(map(lambda pair: pair[0], pairs), cell_width)
    print_table_separator(len(pairs), cell_width)
    print_table_row(map(lambda pair: pair[1], pairs), cell_width)
    print()


def output_generator_powers(powers, modulo):
    items = [(y, x) for x, y in powers.items()]
    cell_width = int(math.log(modulo, 10)) + 1
    items.sort(key=lambda x: x[0])
    output_pairs_table(items, cell_width)
    items.sort(key=lambda x: x[1])
    output_pairs_table(items, cell_width)


modulo = int(sys.argv[1])
generator = int(sys.argv[2])
beta = int(sys.argv[3])
m = int(math.sqrt(modulo - 1)) + 1
generator_powers = {(generator**i % modulo): i for i in range(0, m)}
output_generator_powers(generator_powers, modulo)
gen_inverse = mod_pow(generator, -m, modulo)
print(f"Generator raised to -m: {gen_inverse}\n")
gammas = []
logarithm = 0

for i in range(0, m):
    gamma = beta*(gen_inverse**i) % modulo
    gammas.append((i, gamma))
    if gamma in generator_powers:
        logarithm = generator_powers[gamma] + m*i
        break

output_pairs_table(gammas, int(math.log(modulo, 10)) + 1)
print(f"Logarithm: {logarithm}")
