# File: sc_15_08_tower_of_hanoi.py
"""
Tower of Hanoi - The classic recursion problem
Demonstrates the power and elegance of recursive thinking
"""

print("=" * 60)
print("TOWER OF HANOI - The Classic Recursion Problem")
print("=" * 60)

print("\n" + "-" * 60)
print("THE PROBLEM")
print("-" * 60)
print("""
Setup:
  - Three pegs: SOURCE, AUXILIARY, DESTINATION
  - N disks of different sizes on SOURCE peg
  - Disks are stacked largest to smallest (bottom to top)
  
Goal:
  - Move all disks from SOURCE to DESTINATION
  
Rules:
  1. Only one disk can be moved at a time
  2. A disk can only be placed on top of a larger disk
  3. No larger disk can be placed on a smaller disk
  
Visual example with 3 disks:

  Initial state:        Goal state:
  
  SOURCE  AUX  DEST     SOURCE  AUX  DEST
    |      |     |         |      |     |
    █      |     |         |      |     █
   ███     |     |         |      |    ███
  █████    |     |         |      |   █████
  ──────────────────     ──────────────────
""")

print("\n" + "-" * 60)
print("THE RECURSIVE INSIGHT")
print("-" * 60)
print("""
The key insight: To move N disks from SOURCE to DESTINATION:

  1. Move N-1 disks from SOURCE to AUXILIARY
     (using DESTINATION as temporary storage)
     
  2. Move the largest disk from SOURCE to DESTINATION
     (Now it's in the right place!)
     
  3. Move N-1 disks from AUXILIARY to DESTINATION
     (using SOURCE as temporary storage)

Base case: Moving 1 disk is trivial - just move it!

This breaks down a complex problem into:
  - Two smaller versions of the same problem (steps 1 & 3)
  - One simple action (step 2)
""")

print("\n" + "=" * 60)
print("THE RECURSIVE SOLUTION")
print("=" * 60)

def tower_of_hanoi(n, source, destination, auxiliary, moves=None):
    """
    Solve Tower of Hanoi problem recursively
    
    Args:
        n: Number of disks to move
        source: Name of source peg
        destination: Name of destination peg
        auxiliary: Name of auxiliary peg
        moves: List to store all moves (for counting)
    
    Returns:
        List of all moves
    """
    if moves is None:
        moves = []
    
    if n == 1:  # BASE CASE: Only one disk - just move it!
        move = f"Move disk 1 from {source} to {destination}"
        moves.append(move)
        print(move)
    else:  # RECURSIVE CASE: Break down into smaller problems
        # Step 1: Move n-1 disks from source to auxiliary
        tower_of_hanoi(n - 1, source, auxiliary, destination, moves)
        
        # Step 2: Move the largest disk from source to destination
        move = f"Move disk {n} from {source} to {destination}"
        moves.append(move)
        print(move)
        
        # Step 3: Move n-1 disks from auxiliary to destination
        tower_of_hanoi(n - 1, auxiliary, destination, source, moves)
    
    return moves

print("\n" + "-" * 60)
print("Example 1: Solving with 3 disks")
print("-" * 60)
moves = tower_of_hanoi(3, "SOURCE", "DESTINATION", "AUXILIARY")
print(f"\nTotal moves: {len(moves)}")
print(f"Formula verification: 2^3 - 1 = {2**3 - 1}")

print("\n" + "-" * 60)
print("Example 2: Solving with 4 disks")
print("-" * 60)
moves = tower_of_hanoi(4, "A", "C", "B")
print(f"\nTotal moves: {len(moves)}")
print(f"Formula verification: 2^4 - 1 = {2**4 - 1}")

print("\n" + "=" * 60)
print("UNDERSTANDING THE FORMULA: 2^n - 1")
print("=" * 60)

print("\nWhy does it take exactly 2^n - 1 moves?")
print("-" * 60)
print("""
Let T(n) = minimum moves to solve n disks

For n=1: T(1) = 1 move (just move the disk)

For n>1: T(n) = T(n-1) + 1 + T(n-1)
         = 2*T(n-1) + 1

This gives us:
  T(1) = 1
  T(2) = 2*1 + 1 = 3
  T(3) = 2*3 + 1 = 7
  T(4) = 2*7 + 1 = 15
  ...
  
Pattern: T(n) = 2^n - 1
""")

print("\nMinimum moves required for different n:")
print("-" * 60)
for n in range(1, 11):
    min_moves = 2**n - 1
    print(f"  {n:2d} disk(s): {min_moves:6d} moves", end="")
    if n <= 3:
        print()
    elif n == 5:
        print("  (~30 seconds at 1 move/second)")
    elif n == 10:
        print("  (~17 minutes at 1 move/second)")
    else:
        print()

print("\nFor larger numbers of disks:")
print("-" * 60)
interesting_cases = [
    (20, "~12 days"),
    (30, "~34 years"),
    (40, "~35,000 years"),
    (64, "~585 billion years - longer than age of universe!")
]

for n, time_str in interesting_cases:
    moves = 2**n - 1
    print(f"  {n} disks: {moves:,} moves ({time_str})")

print("\n" + "=" * 60)
print("VISUALIZING THE RECURSION")
print("=" * 60)

def tower_of_hanoi_trace(n, source, dest, aux, indent=0):
    """Tower of Hanoi with indentation to show recursion depth"""
    prefix = "  " * indent
    
    if n == 1:
        print(f"{prefix}Move disk 1: {source} → {dest}")
    else:
        print(f"{prefix}[Moving {n} disks from {source} to {dest} using {aux}]")
        print(f"{prefix}Step 1: Move {n-1} disks {source} → {aux}")
        tower_of_hanoi_trace(n - 1, source, aux, dest, indent + 1)
        
        print(f"{prefix}Step 2: Move disk {n}: {source} → {dest}")
        
        print(f"{prefix}Step 3: Move {n-1} disks {aux} → {dest}")
        tower_of_hanoi_trace(n - 1, aux, dest, source, indent + 1)

print("\nVisualizing recursion for 3 disks:")
print("-" * 60)
tower_of_hanoi_trace(3, "S", "D", "A")

print("\n" + "=" * 60)
print("WHY TOWER OF HANOI IS IMPORTANT")
print("=" * 60)
print("""
Educational value:
  • Perfect example of "divide and conquer" strategy
  • Shows how recursion can elegantly solve complex problems
  • Demonstrates exponential growth (2^n)
  • Illustrates the power of recursive thinking
  
Real-world applications:
  • Backup rotation strategies
  • Disk scheduling algorithms
  • Puzzle solving algorithms
  • Understanding exponential complexity
  
Key lessons:
  • Some problems are MUCH easier to solve recursively
  • Recursive solutions can be surprisingly short
  • But they can have exponential time complexity
  • Always consider if the elegant solution is also practical
""")

print("\n" + "=" * 60)
print("ITERATIVE SOLUTION?")
print("=" * 60)
print("""
Can Tower of Hanoi be solved iteratively?

Yes, but it's much more complex!

Iterative approach requires:
  • Tracking state of all three pegs
  • Complex logic for which disk to move next
  • Special rules (odd vs even number of disks)
  • Much longer and harder to understand code

The recursive solution is ~15 lines.
The iterative solution is ~50+ lines.

This is a perfect example where recursion shines!
""")

print("\n" + "=" * 60)
print("TRY IT YOURSELF")
print("=" * 60)

print("\nExercise 1: Count the moves at each level")
print("-" * 40)
print("Modify the function to track how many moves")
print("happen at each recursion depth level.")

print("\nExercise 2: Visual simulation")
print("-" * 40)
print("Create a version that shows the state of all")
print("three pegs after each move.")

print("\nExercise 3: Verify the formula")
print("-" * 40)
print("Write a function that counts moves without printing")
print("and verify that it always equals 2^n - 1")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Tower of Hanoi is the CLASSIC recursive problem
2. The recursive solution is elegant and short
3. To move n disks: move n-1, move largest, move n-1
4. Minimum moves: 2^n - 1 (exponential!)
5. Some problems are MUCH easier with recursion
6. Always the same pattern: base case + recursive case
7. Recursion shines when problem has recursive structure

This is why computer scientists love this puzzle -
it perfectly demonstrates the power and elegance
of recursive thinking!
""")
