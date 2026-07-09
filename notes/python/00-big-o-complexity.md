# Big-O / Time & Space Complexity

## What is Big-O Notation?

Big-O notation describes how the runtime or memory usage of an algorithm grows as the input size (`n`) grows. It doesn't measure exact seconds — it measures the *rate of growth*.

---

## Why does it matter?

Two algorithms can solve the same problem, but one might slow to a crawl on large inputs while the other stays fast. Big-O lets you predict and compare that behavior *before* running the code, which matters when you're choosing data structures or writing production-scale backend logic.

---

## Key Concepts

- **Time Complexity** — how runtime grows with input size
- **Space Complexity** — how memory usage grows with input size
- **Worst Case** — Big-O almost always describes the worst-case scenario
- **Growth Rate** — we care about the trend as `n → ∞`, not small-input performance

---

## Common Complexities (Best to Worst)

| Notation     | Name         | Example                          |
|--------------|--------------|-----------------------------------|
| O(1)         | Constant     | Accessing an array element by index |
| O(log n)     | Logarithmic  | Binary search                    |
| O(n)         | Linear       | Looping through a list           |
| O(n log n)   | Linearithmic | Merge sort, quick sort (avg)     |
| O(n²)        | Quadratic    | Nested loops (e.g. bubble sort)  |
| O(2ⁿ)        | Exponential  | Naive recursive Fibonacci        |
| O(n!)        | Factorial    | Generating all permutations      |

---

## Time & Space Complexity

| Operation                     | Time     | Space |
|--------------------------------|----------|-------|
| Access array element by index  | O(1)     | O(1)  |
| Linear search                  | O(n)     | O(1)  |
| Binary search                  | O(log n) | O(1)  |
| Nested loop over `n` items     | O(n²)    | O(1)  |

---

## Example (Python)

```python
# O(1) - constant time
def get_first(arr):
    return arr[0]

# O(n) - linear time
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - quadratic time
def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
```

---

## Rules of Thumb

- Drop constants: `O(2n)` becomes `O(n)`
- Drop lower-order terms: `O(n² + n)` becomes `O(n²)`
- Different inputs get different variables: `O(a + b)`, not `O(2n)`, if two separate arrays are involved

---

## Common Use Cases

- Comparing algorithm efficiency before implementation
- Choosing the right data structure for a problem
- Explaining trade-offs in code reviews or interviews

---

## Summary

Big-O notation is the language used to describe how an algorithm scales. Every DSA topic that follows — arrays, recursion, sorting, trees — will be explained using this notation, so understanding it now makes everything after it click faster.