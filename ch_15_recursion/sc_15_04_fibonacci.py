# File: sc_15_04_fibonacci.py
"""
Recursion: Fibonacci sequence
Comparing slow recursion, fast iteration, and memoization
"""

print("=" * 60)
print("FIBONACCI - When recursion can be slow")
print("=" * 60)

# SLOW: Simple recursive Fibonacci
def fibonacci_slow(n):
    """
    Simple recursive Fibonacci - but very SLOW!
    Because same subproblems are calculated many times
    """
    if n <= 1:  # BASE CASE
        return n
    else:       # RECURSIVE CASE: Sum of previous two
        return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

print("\n1. Simple recursive Fibonacci (SLOW):")
print("fibonacci_slow(8) =", fibonacci_slow(8))
print("fibonacci_slow(10) =", fibonacci_slow(10))
print("\nWarning: fibonacci_slow(35) would take many seconds!")
print("         fibonacci_slow(40) would take minutes!")

print("\n" + "-" * 60)
print("Why is it so slow?")
print("-" * 60)
print("""
fibonacci_slow(5) calls:
  fibonacci_slow(4) + fibonacci_slow(3)
      fibonacci_slow(3) + fibonacci_slow(2)    [fib(3) calculated here]
          fibonacci_slow(2) + fibonacci_slow(1)
      fibonacci_slow(2) + fibonacci_slow(1)    [fib(3) calculated AGAIN!]

Many calculations are repeated! This grows exponentially.
""")

# SMART: Memoization (caching results)
print("\n" + "-" * 60)
print("2. Fibonacci with Memoization - Dictionary (SMART):")
print("-" * 60)

def fibonacci_memo(n, memo=None):
    """Fibonacci with memoization - stores computed results"""
    if memo is None:
        memo = {}
    
    if n in memo:  # Already computed?
        return memo[n]
    
    if n <= 1:  # BASE CASE
        return n
    
    # Recursive case: Store result before returning
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("fibonacci_memo(10) =", fibonacci_memo(10))
print("fibonacci_memo(50) =", fibonacci_memo(50))
print("fibonacci_memo(100) =", fibonacci_memo(100))

# List-based memoization
print("\n" + "-" * 60)
print("3. Fibonacci with Memoization - List (SMART):")
print("-" * 60)

def fibonacci_memo_list(n):
    """Fibonacci with list-based memoization - preallocated cache"""
    if n <= 1:
        return n
    
    memo = [-1] * (n + 1)  # Preallocate list, -1 = not computed
    memo[0], memo[1] = 0, 1
    
    def helper(k):
        if memo[k] != -1:  # Already computed?
            return memo[k]
        memo[k] = helper(k - 1) + helper(k - 2)
        return memo[k]
    
    return helper(n)

print("fibonacci_memo_list(10) =", fibonacci_memo_list(10))
print("fibonacci_memo_list(50) =", fibonacci_memo_list(50))
print("fibonacci_memo_list(100) =", fibonacci_memo_list(100))

# List-based memoization without helper function
print("\n" + "-" * 60)
print("3b. Fibonacci with List Memoization - No helper (SMART):")
print("-" * 60)

def fibonacci_memo_list_alt(n, memo=None):
    """Fibonacci with list-based memoization - direct recursive"""
    if memo is None:
        memo = [-1] * (n + 1)
        memo[0], memo[1] = 0, 1
    
    if n <= 1:
        return n
    
    if memo[n] != -1:  # Already computed?
        return memo[n]
    
    memo[n] = fibonacci_memo_list_alt(n - 1, memo) + fibonacci_memo_list_alt(n - 2, memo)
    return memo[n]

print("fibonacci_memo_list_alt(10) =", fibonacci_memo_list_alt(10))
print("fibonacci_memo_list_alt(50) =", fibonacci_memo_list_alt(50))
print("fibonacci_memo_list_alt(100) =", fibonacci_memo_list_alt(100))

print("\n" + "-" * 60)
print("What is Memoization?")
print("-" * 60)
print("""
Memoization = Caching results to avoid recalculation

First call to fibonacci_memo(5):
  - Calculates fib(0), fib(1), fib(2), fib(3), fib(4), fib(5)
  - Stores each result in the memo dictionary
  
Second call to fibonacci_memo(5):
  - Looks up the answer in memo
  - Returns immediately without recalculation!
  
This makes recursive Fibonacci fast enough to use.
""")

# FAST: Iterative Fibonacci
print("\n" + "-" * 60)
print("4. Iterative Fibonacci (FAST):")
print("-" * 60)

def fibonacci_fast(n):
    """Efficient iterative Fibonacci using a sliding window"""
    if n <= 1:
        return n
    
    a, b = 0, 1  # a = F(0), b = F(1)
    for _ in range(2, n + 1):
        a, b = b, a + b  # Move the window forward
    return b

print("fibonacci_fast(8) =", fibonacci_fast(8))
print("fibonacci_fast(10) =", fibonacci_fast(10))
print("fibonacci_fast(50) =", fibonacci_fast(50))
print("fibonacci_fast(100) =", fibonacci_fast(100))
print("\nMuch faster! Can handle large numbers easily.")
print("No recursion = No stack limit issues.")

print("\n" + "-" * 60)
print("SUMMARY: Four approaches compared")
print("-" * 60)
print("""
Approach          | Speed      | Elegance | When to use
------------------|------------|----------|---------------------------
Simple recursion  | Very slow  | High     | Never for Fibonacci!
Memo (dict)       | Fast       | High     | When recursion is natural
Memo (list)       | Fast       | High     | Known max n, slight speedup
Iteration         | Very fast  | Medium   | Production code, best choice
""")
