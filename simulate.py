from algo_1 import algo_one_run
from algo_2 import algo_two_run
from generate_uniform_stream import generate_uniform_data

list_a = [4, 6, 8, 10, 12, 16, 20]
list_b = [12500, 8334, 6250, 5000, 4168, 3124, 2500]

sample_times = 5

error_1 = [0 for i in range(len(list_a))]
error_2 = [0 for i in range(len(list_a))]


data_size = 3000000
data_range = 2000

# test on uniform data
for i in range(sample_times):
    print("Progress: " + str(i) + "/" + str(sample_times) + "\n")
    generate_uniform_data(data_size, data_range)
    for j in range(len(list_a)):
        error_1[j] += algo_one_run(list_a[j], list_b[j]) / data_range / sample_times
        error_2[j] += algo_two_run(list_a[j], list_b[j]) / data_range / sample_times

print(error_1)
print("\n")
print(error_2)


