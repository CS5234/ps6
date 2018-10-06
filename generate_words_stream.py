import json
import random

output_file_name = "input.txt"
output_stat_file = "input_stat.txt"


def generate_uniform_data(size, data_range):
    stat = dict()

    output_file = open(output_file_name, "w")

    for i in range(size):
        next_rand = random.randint(0, data_range)
        output_file.write(str(next_rand) + "\n")

        if stat.get(next_rand, ''):
            stat[next_rand] += 1
        else:
            stat[next_rand] = 1

    output_file.close()

    output_stat = open(output_stat_file, "w")

    output_stat.write(json.dumps(stat))

    output_stat.close()

