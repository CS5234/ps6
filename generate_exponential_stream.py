import json
import random

output_file_name = "input.txt"
output_stat_file = "input_stat.txt"


def generate_exponential_data(size, data_range):
    stat = dict()

    output_file = open(output_file_name, "w")

    cons = pow(2, data_range)

    for i in range(size):
        rdm = random.randint(0, cons)
        next_rand = helper(rdm, data_range)
        if next_rand:
            output_file.write(str(next_rand) + "\n")
            if stat.get(next_rand, ''):
                stat[next_rand] += 1
            else:
                stat[next_rand] = 1

    output_file.close()

    output_stat = open(output_stat_file, "w")

    output_stat.write(json.dumps(stat))

    output_stat.close()


def helper(s, data_range):
    const = pow(2, data_range)
    j = 0
    while 1:
        if s - const / 2 <= 0:
            return j
        elif j <= data_range:
            s = s - const / 2
            const = const / 2
            j = j + 1
            continue
        else:
            break


generate_exponential_data(6000000, 24)
