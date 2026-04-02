# Depending on a random selection of a pivot and partitioning the array, the algorithm Randomized Quickselect is used to pick the k th smallest.
# It simply reiterates through a single partition resulting into an anticipated time dimension of O(n).

import random

def randomized_quickselect(arr, k):
    # Handling the base case where the array has only one element
    if len(arr) == 1:
        return arr[0]

    # Picking a random pivot from the array
    pivot = random.choice(arr)

    # Partitioning the array around the pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    # Recursively selecting the correct side of the array
    if k <= len(less_than_pivot):
        return randomized_quickselect(less_than_pivot, k)
    elif k > len(less_than_pivot) + len(equal_to_pivot):
        return randomized_quickselect(greater_than_pivot, k - len(less_than_pivot) - len(equal_to_pivot))
    else:
        return pivot

# Example usage for Randomized Quickselect
arr = [12, 3, 5, 7, 19, 1, 18, 13, 15, 9, 4]
k = 5
result = randomized_quickselect(arr, k)
print(f"The {k}th smallest element using Randomized Quickselect is: {result}")