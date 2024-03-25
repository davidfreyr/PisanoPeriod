from FElem_class import FElem
from collections import Counter


def encode(a1, b1, a2, b2, p):
    return a1 * p ** 3 + b1 * p ** 2 + a2 * p + b2


def decode(i, p):
    a1, rem1 = divmod(i, p ** 3)
    b1, rem2 = divmod(rem1, p ** 2)
    a2, b2 = divmod(rem2, p)
    return a1, b1, a2, b2

# generate the permutation list for F_{p^2}
def generate_field_permutation_updated_correctly(p):
    field_permutation = [None] * (p ** 4)
    for i in range(p ** 4):
        a1, b1, a2, b2 = decode(i, p)
        x = FElem(a1, b1, p)
        y = FElem(a2, b2, p)
        z1 = y
        z2 = x + y
        z_encoded = encode(z1.a, z1.b, z2.a, z2.b, p)
        field_permutation[i] = z_encoded
    return field_permutation

# find cycles in a permutation list
def find_cycles(permutation):
    cycles = []
    visited = set()
    for i in range(len(permutation)):
        if i in visited:
            continue
        cycle = []
        current = i
        while current not in visited:
            visited.add(current)
            cycle.append(current)
            current = permutation[current]
        cycles.append(cycle)
    return cycles

# decode only the y value from an encoded number
def decode_y(i, p):
    _, rem1 = divmod(i, p ** 3)
    _, rem2 = divmod(rem1, p ** 2)
    a2, b2 = divmod(rem2, p)
    return FElem(a2, b2, p)


def lengths(cycles):
    lens = []
    for c in cycles:
        lens.append(len(c))
    return Counter(lens)

p = 53
field_permutation_updated_correctly = generate_field_permutation_updated_correctly(p)

cycles_updated = find_cycles(field_permutation_updated_correctly)

decoded_cycles = [[str(decode_y(i, p)) for i in cycle] for cycle in cycles_updated]

print(Counter(lengths(decoded_cycles)))
