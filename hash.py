from constants import a, b

prime_factor = 101723


def get_param_a(i):
    return a[i]


def get_param_b(i):
    return b[i]


def uniform_hash(x, m, index):
    return int(((get_param_a(index) * x + get_param_b(index)) % prime_factor) % m)


