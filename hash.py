import hashlib

from constants import a, b

prime_factor = 101723


def get_param_a(i):
    return a[i]


def get_param_b(i):
    return b[i]


def uniform_hash(x, m, index):
    return int(((get_param_a(index) * x + get_param_b(index)) % prime_factor) % m)


def hash_string(x, m):
    return int(hashlib.sha256(x.encode('utf-8')).hexdigest(), 16) % m;
