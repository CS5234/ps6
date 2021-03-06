import json
from statistics import median

from hash import uniform_hash

size_a = 10
size_b = 2500

input_file = "input.txt"
input_stat_file = "input_stat.txt"

ab_counter = [[0 for i in range(size_b)] for j in range(size_a)]


def run():
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
            j = uniform_hash(int(key), size_b, i)
            if j % 2 == 0:
                neighbour = ab_counter[i][j+1]
            else:
                neighbour = ab_counter[i][j-1]

            estimated = ab_counter[i][j] - neighbour

            estimated_lst.append(estimated)

        print("value: " + key + " estimated: " + str(median(estimated_lst)) + " actual:" + str(actual))
        print(estimated_lst)
        error += abs(median(estimated_lst) - actual)

    print("error is " + str(error / 1000))

run()




