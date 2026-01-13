# File: sc_15_05_concepts.py
"""
Recursion: Fundamental concepts
Base case, recursive case, and the call stack
"""

print("=" * 60)
print("FUNDAMENTAL RECURSION CONCEPTS")
print("=" * 60)

print("\n" + "=" * 60)
print("1. BASE CASE (Basis-tilfelle)")
print("=" * 60)
print("""
The BASE CASE is the simplest version of the problem that can be 
solved directly, WITHOUT recursion.

Why it's critical:
  - Without a base case, recursion never stops (infinite loop!)
  - It's the "exit condition" that prevents stack overflow
  - It's where the recursion "bottoms out"
  
Examples:
  countdown(n):     base case is n == 0
  factorial(n):     base case is n == 0 or n == 1
  fibonacci(n):     base case is n <= 1
""")

print("\n" + "=" * 60)
print("2. RECURSIVE CASE (Rekursivt tilfelle)")
print("=" * 60)
print("""
The RECURSIVE CASE is where the function calls itself with a 
SIMPLER version of the problem.

Key principle: MUST move toward the base case!

Examples:
  countdown(n):     calls countdown(n-1)    [n gets smaller]
  factorial(n):     calls factorial(n-1)    [n gets smaller]
  fibonacci(n):     calls fib(n-1) + fib(n-2)  [n gets smaller]
  
If your recursive case doesn't move toward the base case,
you'll get infinite recursion!
""")

print("\n" + "=" * 60)
print("3. THE CALL STACK (Kallstakk)")
print("=" * 60)
print("""
The CALL STACK is how Python keeps track of function calls.

How it works:
  1. Each function call adds a new "layer" (frame) to the stack
  2. When a function returns, its layer is removed
  3. The result is passed back to the previous layer
  
Visualization for factorial(3):
  
  [factorial(3)]                  Stack grows
  [factorial(2)]                      ↓
  [factorial(1)]     ← Base case reached! Returns 1
  [factorial(2)]     ← 2 * 1 = 2, returns 2
  [factorial(3)]     ← 3 * 2 = 6, returns 6
                                      ↑
                                  Stack unwinds
  
Python's stack limit: ~1000 function calls
  (You can increase it, but be careful!)
""")

# Demonstrate call stack with a simple example
print("\n" + "-" * 60)
print("Demonstrating call stack depth:")
print("-" * 60)

import sys
print(f"Current recursion limit: {sys.getrecursionlimit()}")

def show_depth(n, max_n):
    """Show how deep we are in the call stack"""
    if n == 0:
        print(f"  {'  ' * max_n}Reached base case at depth {max_n}!")
        return "BASE"
    else:
        print(f"  {'  ' * (max_n - n)}Entering depth {max_n - n + 1}")
        result = show_depth(n - 1, max_n)
        print(f"  {'  ' * (max_n - n)}Leaving depth {max_n - n + 1}")
        return result

print("\nCall stack for show_depth(3):")
show_depth(3, 3)

print("\n" + "=" * 60)
print("4. COMMON PITFALLS")
print("=" * 60)
print("""
PITFALL 1: Missing base case
  def bad_countdown(n):
      print(n)
      bad_countdown(n - 1)  # Never stops! No base case!
  
PITFALL 2: Base case never reached
  def bad_fibonacci(n):
      if n == 0:
          return 0
      return bad_fibonacci(n - 1) + bad_fibonacci(n + 1)  # n + 1 goes WRONG way!
  
PITFALL 3: Stack overflow
  # Calling with too large n causes stack overflow
  factorial(10000)  # Will crash!
  
PITFALL 4: Inefficiency
  # Simple recursive Fibonacci is exponentially slow
  fibonacci_slow(40)  # Takes forever!
""")

print("\n" + "=" * 60)
print("5. RECURSION CHECKLIST")
print("=" * 60)
print("""
Before writing a recursive function, ask:

☐ What is my BASE CASE?
  - Can I solve the simplest version directly?
  
☐ What is my RECURSIVE CASE?
  - How do I break down the problem into smaller pieces?
  
☐ Am I moving TOWARD the base case?
  - Does the problem get simpler with each call?
  
☐ What will I RETURN?
  - Does each recursive call return a value I can use?
  
☐ Is recursion the RIGHT choice?
  - Could a simple loop be clearer and faster?
""")
