# file: sc_11_08_reading_text_examples.py

from pathlib import Path

# Get the script directory
script_dir = Path(__file__).parent

# ===== EXAMPLE 1: Reading names (simple text) =====
print("=== Example 1: Reading names ===")

# Create data file with with-as
names_file = script_dir / "names.txt"
with names_file.open('w', encoding='utf-8') as f:
    f.write("Anna\n")
    f.write("Bob\n")
    f.write("Charlie\n")
    f.write("Diana\n")

# Read and process
with names_file.open('r', encoding='utf-8') as f:
    content = f.read()

# Split into list and process
names = content.split('\n')
names = [name for name in names if name]  # Remove empty strings

print(f"Found {len(names)} names:")
for name in names:
    print(f"  - {name}")


# ===== EXAMPLE 2: Reading numbers from comma-separated values =====
print("\n=== Example 2: Reading numbers (CSV format) ===")

# Create data file with pathlib
numbers_file = script_dir / "numbers.txt"
numbers_file.write_text("10, 25, 30, 45, 50, 12, 8")

# Read and process numbers
content = numbers_file.read_text()
number_strings = content.split(',')
numbers = [int(num.strip()) for num in number_strings]

print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.1f}")
print(f"Max: {max(numbers)}")


# ===== EXAMPLE 3: Reading structured data (name and score) =====
print("\n=== Example 3: Reading structured data ===")

# Create data file with with-as
scores_file = script_dir / "scores.txt"
with scores_file.open('w', encoding='utf-8') as f:
    f.write("Anna: 85\n")
    f.write("Bob: 92\n")
    f.write("Charlie: 78\n")
    f.write("Diana: 95\n")

# Read and process
with scores_file.open('r', encoding='utf-8') as f:
    lines = f.readlines()

# Parse data
student_scores = []
for line in lines:
    line = line.strip()
    if line:
        parts = line.split(':')
        name = parts[0].strip()
        score = int(parts[1].strip())
        student_scores.append([name, score])

print("Student scores:")
for student in student_scores:
    print(f"  {student[0]}: {student[1]} points")

# Find best student
best_score = 0
best_student = ""
for student in student_scores:
    if student[1] > best_score:
        best_score = student[1]
        best_student = student[0]

print(f"\nBest student: {best_student} with {best_score} points")


# ===== EXAMPLE 4: Reading multiple numbers per line =====
print("\n=== Example 4: Reading multiple numbers per line ===")

# Create data file with pathlib
matrix_file = script_dir / "matrix.txt"
matrix_file.write_text("1 2 3\n4 5 6\n7 8 9")

# Read and process as 2D list
with matrix_file.open('r', encoding='utf-8') as f:
    lines = f.readlines()

matrix = []
for line in lines:
    row = [int(num) for num in line.split()]
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Calculate sum of each row
print("\nRow sums:")
for i in range(len(matrix)):
    row_sum = sum(matrix[i])
    print(f"  Row {i + 1}: {row_sum}")


print("\n--- All examples completed ---")
