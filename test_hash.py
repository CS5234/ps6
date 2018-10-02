import random
import numpy as np


from hash import uniform_hash


def test_uniform_hash(test_range):
    stat_lst = [0 for i in range(test_range)]
    for i in range(test_range * 100):
        v = random.randint(0, 0xffffffffffffffff)
        stat_lst[uniform_hash(v, test_range, 2)] += 1
    print(stat_lst)
    print("\n")
    print("variance is " + str(np.var(stat_lst)))


def test_sequence(times):
    for i in range(times):
        v = random.randint(1, 10000)
        print("index " + str(i) + "\n")
        for k in range(10):
            print(str(uniform_hash(v, 10000, k)) + " ")


test_uniform_hash(1000)