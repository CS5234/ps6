import io
import json
import math
import random

output_file_name = "input_exponential.txt"
output_stat_file = "input_exponential_stat.txt"


def random_expo(a, b):
    rand_val = random.randint(a, 2 ** (b + 1) - 1)
    if rand_val == 0:
        return rand_val
    else:
        return int(math.log(rand_val, 2))


def generate_data(n, m):
    stat = dict()

    output_file = io.open(output_file_name, 'w')

    for i in range(n):
        next_rand = random_expo(0, m - 1)
        output_file.write((str(next_rand) + "\n").decode('utf-8'))

        if stat.get(next_rand, ''):
            stat[next_rand] += 1
        else:
            stat[next_rand] = 1

    output_file.close()

    output_stat = io.open(output_stat_file, 'w')
    output_stat.write(json.dumps(stat).decode('utf-8'))
    output_stat.close()


generate_data(10000000, 30)
