# File: sc_15_03_factorial.py
"""
Recursion: Factorial (n!)
Computing factorials with recursion and tail recursion
"""

print("=" * 60)
print("FACTORIAL (n!) - Computing factorials")
print("=" * 60)

def factorial(n):
    """Calculate n! (n factorial)"""
    if n == 0 or n == 1:  # BASE CASE
        return 1
    else:                 # RECURSIVE CASE: n * (n-1)!
        return n * factorial(n - 1)

print("\nStandard recursive factorial:")
print("factorial(5) =", factorial(5))
print("Explanation: 5! = 5 × 4 × 3 × 2 × 1 = 120")

print("\n" + "-" * 60)
print("TAIL RECURSION - Accumulator Pattern")
print("-" * 60)

def factorial_tail(n, acc=1):
    """
    Tail recursive factorial - computes multiplication BEFORE the call
    (accumulator pattern)
    """
    if n == 0 or n == 1:  # BASE CASE
        return acc
    else:                 # RECURSIVE CASE: The call is the last operation
        return factorial_tail(n - 1, acc * n)

print("\nTail recursive factorial:")
print("factorial_tail(5) =", factorial_tail(5))

print("\n" + "-" * 60)
print("What is Tail Recursion?")
print("-" * 60)
print("""
A function is TAIL RECURSIVE if the recursive call is the
very last operation in the function.

Standard recursion:
  factorial(5) → 5 * factorial(4)  [multiplication AFTER return]

Tail recursion:
  factorial_tail(5, 1) → factorial_tail(4, 5)  [multiplication BEFORE call]
  
Advantage:
  - Some languages can optimize tail recursion to avoid stack growth
  - Python doesn't optimize it, but the pattern is useful to know
  - Can be converted to iteration more easily
""")

print("\nIterative equivalent of tail recursion:")
def factorial_iter(n):
    """Iterative factorial using accumulator pattern"""
    acc = 1
    while n > 1:
        acc = acc * n
        n = n - 1
    return acc

print("factorial_iter(5) =", factorial_iter(5))
