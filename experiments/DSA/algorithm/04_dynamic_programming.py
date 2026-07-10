"""
Dynamic Programming (DP) — Practice
---------------------------------------
DP means breaking a problem into smaller overlapping subproblems,
solving each one only once, and saving ("memoizing") the result
so we never redo the same work.
"""
from datetime import datetime

# ---------------------------------------------------------
# Problem 1: Fibonacci
...
def fib_slow(n):
    if n<=1:
        return 1
    return fib_slow(n-1)+fib_slow(n-2)

# Now with memoization (a dictionary to store answers) -> O(n)
def fib_fast(n,memo=None):
    if memo is None:
        memo = {}
    if n<=1:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n] = fib_fast(n-1,memo)+fib_fast(n-2,memo)
    return memo[n]

if __name__ == "__main__":
    n = 15
    s1=datetime.now()
    print(f"fib_slow({n}):", fib_slow(n))
    e1=datetime.now()
    print(f"slow {e1-s1}")
    s2=datetime.now()
    print(f"fib_fast({n}):", fib_fast(n))
    e2=datetime.now()
    print(f"fast {e2-s2}")