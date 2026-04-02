# The Median of Medians algorithm discovers the k th smallest number in an array by splitting the array into 5-groups, sorting each group, and recursively computing the median of the medians.
# The worst case time complexity will be O(n).

import random
def median_of_medians(arr, k):
    # Handling the case for small arrays
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    # Dividing the array into groups of 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Finding the median of each group
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Recursively finding the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partitioning the array based on the pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    # Deciding which part of the array to recurse on
    if len(less_than_pivot) >= k:
        return median_of_medians(less_than_pivot, k)
    elif len(less_than_pivot) + len(equal_to_pivot) >= k:
        return pivot
    else:
        return median_of_medians(greater_than_pivot, k - len(less_than_pivot) - len(equal_to_pivot))

# Example usage for Median of Medians
arr = [12, 3, 5, 7, 19, 1, 18, 13, 15, 9, 4]
k = 5
result = median_of_medians(arr, k)
print(f"The {k}th smallest element using Median of Medians is: {result}")