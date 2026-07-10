"""
Brute Force Algorithms — Practice
------------------------------------
Brute force means trying every possible option, with no shortcuts.
Simple to write, but often slow (usually O(n^2) or worse).

This file solves a few basic problems using brute force,
as a baseline to compare with smarter methods later.
"""

# ---------------------------------------------------------
# Problem 1: Check if an array has any duplicate values
# Compare every pair -> O(n^2)
# ---------------------------------------------------------
def has_duplicate_brute(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# ---------------------------------------------------------
# Problem 2: Find two numbers that add up to a target
# Check every pair -> O(n^2)
# ---------------------------------------------------------
def two_sum_brute(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

# ---------------------------------------------------------
# Problem 3: Find the maximum value in an array
# Check every value once -> O(n)
# (Still brute force, just not O(n^2) — sometimes checking
# everything once is the only way)
# ---------------------------------------------------------
def find_max_brute(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


if __name__ == "__main__":
    data = [4, 2, 7, 2, 9]
    print("Array:", data)
    print("Has duplicate?", has_duplicate_brute(data))
    print("Two numbers summing to 11:", two_sum_brute(data, 11))
    print("Max value:", find_max_brute(data))