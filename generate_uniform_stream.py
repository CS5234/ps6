import json
import random

from constants import data_range

output_file_name = "input.txt"
output_stat_file = "input_stat.txt"


def generate_data(size, stream_range):
    stat = dict()

    output_file = open(output_file_name, "w")

    for i in range(size):
        next_rand = random.randint(0, stream_range)
        output_file.write(str(next_rand) + "\n")

        if stat.get(next_rand, ''):
            stat[next_rand] += 1
        else:
            stat[next_rand] = 1

    output_file.close()

    output_stat = open(output_stat_file, "w")

    output_stat.write(json.dumps(stat))

    output_stat.close()


generate_data(10, 1000000)
