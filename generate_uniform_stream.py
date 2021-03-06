import io
import json
import random

output_file_name = "input_uniform.txt"
output_stat_file = "input_uniform_stat.txt"


def generate_data(n, m):
    stat = dict()

    output_file = io.open(output_file_name, 'w')

    for i in range(n):
        next_rand = random.randint(0, m - 1)
        output_file.write((str(next_rand) + "\n").decode('utf-8'))

        if stat.get(next_rand, ''):
            stat[next_rand] += 1
        else:
            stat[next_rand] = 1

    output_file.close()

    output_stat = io.open(output_stat_file, 'w')
    output_stat.write(json.dumps(stat).decode('utf-8'))
    output_stat.close()


generate_data(10000000, 1000)
