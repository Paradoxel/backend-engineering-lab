"""
Backtracking — Practice (Simple Version)
---------------------------------------------
Backtracking means building a solution step by step, and
undoing ("backtracking") the last choice to try another one.

This file solves the simplest backtracking problem: finding
every possible subset of a list of numbers.
"""

def find_subsets(nums):
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])  # found one full subset
            return

        # choice 1: don't include nums[index]
        backtrack(index + 1, current)

        # choice 2: include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()  # undo the choice (backtrack)

    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    subsets = find_subsets(nums)

    print(f"All subsets of {nums}:")
    for s in subsets:
        print(" ", s)