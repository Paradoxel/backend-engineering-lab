"""
Divide and Conquer Algorithms — Practice
--------------------------------------------
Divide and conquer means splitting a problem into smaller pieces,
solving each piece, then combining the results.

This file covers two classic examples: Binary Search and Merge Sort.
"""

# ---------------------------------------------------------
# Problem 1: Binary Search
# Find a target value in a SORTED array.
# Cut the search space in half each step -> O(log n)
# ---------------------------------------------------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



if __name__ == "__main__":
    sorted_data = [1, 3, 5, 7, 9, 11, 13]
    print("Sorted array:", sorted_data)
    print("Search for 7:", binary_search(sorted_data, 7))
    print("Search for 4:", binary_search(sorted_data, 4))

    unsorted_data = [5, 2, 9, 1, 5, 6]
    print("\nUnsorted array:", unsorted_data)