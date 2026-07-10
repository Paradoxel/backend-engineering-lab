"""
Arrays in Python (list) — Time Complexity & Internals Reference
--------------------------------------------------------------------
Python's built-in `list` is a dynamic array under the hood.
This file uses the built-in list methods directly, and also proves
some internal behavior (memory growth, contiguous access) using
sys.getsizeof and id().

Operation Summary:
| Method                  | Time       |
|--------------------------|------------|
| arr[i]                   | O(1)       |
| arr[i] = value           | O(1)       |
| arr.index(value)         | O(n)       |
| arr.append(value)        | O(1)*      |
| arr.insert(index, value)     | O(n)       |
| arr.pop()                | O(1)       |
| arr.pop(index)               | O(n)       |
| arr.reverse()            | O(n)       |
| arr.sort()               | O(n log n) |
| value in arr             | O(n)       |
| arr[a:b] (slicing)       | O(k)       |

*Amortized — occasionally O(n) when internal resizing happens.
"""


arr = [10,20,30]

print("Initial array:",arr)

# O(1) direct access
print("Access index 1:",arr[1])

# O(1) direct index to write
arr[1]=99
print("After arr[1]=99:",arr)

# O(n) must scan elements 
print("Index of 30:",arr.index(30))

# O(1) 
arr.append(40)
print("After append(40):",arr)

# O(n) must scan elements
arr.insert(1,5)
print("After insert(0,5):",arr)

# O(1) just remove last item
arr.pop()
print("After pop():",arr)

# O(n) must scan all elements
arr.pop(0)
print("After pop(0):",arr)


# O(n) touches every elements once
arr.reverse()
print("After reverser():",arr)

# O(n log n) - Python uses Timsort internally
arr.sort()
print("After sort():", arr)


# O(n) 
print("Is 20 in arr?:",20 in arr)


# ---------------------------------------------------------
# Slicing — O(k), where k is the size of the slice
# ---------------------------------------------------------
arr = [10, 20, 30, 40, 50]
print("\nSlice arr[1:4]:", arr[1:4])   # [20, 30, 40]
print("Slice arr[:3]:", arr[:3])       # [10, 20, 30]
print("Slice arr[::-1] (reverse copy):", arr[::-1])



# Address in memory
sample = [100, 200, 300]
print("\nMemory address of sample[0]:", id(sample[0]))
print("Memory address of sample[1]:", id(sample[1]))

