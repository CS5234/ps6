import json
from statistics import median

from hash import uniform_hash


def algo_one_run(size_a, size_b):
    input_file = "input.txt"
    input_stat_file = "input_stat.txt"

    ab_counter = [[0 for i in range(size_b)] for j in range(size_a)]
    input_stream = open(input_file, "r")

    while True:
        next_input = input_stream.readline()

        if next_input == "":
            break

        next_input = float(next_input)

        for i in range(size_a):
            ab_counter[i][uniform_hash(next_input, size_b, i)] += 1

    input_stat = open(input_stat_file, "r")
    stat = json.loads(input_stat.readline())

    error = 0

    for key in stat.keys():
        actual = stat[key]
        estimated_lst = []
        for i in range(size_a):
            estimated = ab_counter[i][uniform_hash(int(key), size_b, i)]
            estimated_lst.append(estimated)

        print("value: " + key + " estimated: " + str(median(estimated_lst)) + " actual:" + str(actual))
        print(estimated_lst)
        error += abs(median(estimated_lst) - actual)

    return error

