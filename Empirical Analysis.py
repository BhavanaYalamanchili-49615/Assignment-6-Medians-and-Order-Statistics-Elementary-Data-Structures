# The test on the implementation was to test the Median of Medians and Randomized Quickselect algorithms with arrays of various sizes.
# The time of each algorithm was measured and compared by picking the mid-point element in each array.

import random
import time


# Function for Median of Medians algorithm
def median_of_medians(arr, k):
    # Handling small arrays by sorting them and returning the middle element
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    # Dividing the array into groups of 5 elements
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Finding the median of each group
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Recursively finding the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partitioning the array into elements less than, equal to, and greater than the pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    # Recursively finding the k-th element in the correct partition
    if len(less_than_pivot) >= k:
        return median_of_medians(less_than_pivot, k)
    elif len(less_than_pivot) + len(equal_to_pivot) >= k:
        return pivot
    else:
        return median_of_medians(greater_than_pivot, k - len(less_than_pivot) - len(equal_to_pivot))


# Function for Randomized Quickselect algorithm
def randomized_quickselect(arr, k):
    # Handling the base case where only one element is in the array
    if len(arr) == 1:
        return arr[0]

    # Picking a random pivot from the array
    pivot = random.choice(arr)

    # Partitioning the array around the pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    # Recursively selecting the correct partition
    if k <= len(less_than_pivot):
        return randomized_quickselect(less_than_pivot, k)
    elif k > len(less_than_pivot) + len(equal_to_pivot):
        return randomized_quickselect(greater_than_pivot, k - len(less_than_pivot) - len(equal_to_pivot))
    else:
        return pivot


# Empirical Test: Compare Median of Medians and Randomized Quickselect
sizes = [100, 1000, 10000]  # Different input sizes
for size in sizes:
    arr = [random.randint(1, 1000) for _ in range(size)]  # Generating a random array

    k = size // 2  # Selecting the middle element as an example

    # Testing Median of Medians
    start_time = time.time()
    result_median_of_medians = median_of_medians(arr, k)
    end_time = time.time()
    print(f"Median of Medians for n={size}: {end_time - start_time:.5f} seconds")

    # Testing Randomized Quickselect
    start_time = time.time()
    result_randomized_quickselect = randomized_quickselect(arr, k)
    end_time = time.time()
    print(f"Randomized Quickselect for n={size}: {end_time - start_time:.5f} seconds")