# file: sc_11_07_pathlib_examples_2.py
from pathlib import Path

# ===== PATH INFORMATION =====

p = Path("folder/myfile.txt") 
print(f"Full path: {p}") # Full path: folder\myfile.txt
print(f"Name (with extension): {p.name}") # Name (with extension): myfile.txt
print(f"Stem (without extension): {p.stem}") # Stem (without extension): myfile 
print(f"Suffix (extension): {p.suffix}") # Suffix (extension): .txt
print(f"Parent directory: {p.parent}") # Parent directory: folder
print(f"All parts of path: {p.parts}") # All parts of path: ('folder', 'myfile.txt')

# ===== PATH CHECKING =====

# Create a test file to demonstrate checking methods
script_dir = Path(__file__).resolve().parent
test_file = script_dir / "test_demo.txt"
test_file.write_text("This is a test file for demonstration.")

# Check if path exists
print(f"Does '{test_file.name}' exist? {test_file.exists()}")

# Check if it's a file
print(f"Is it a file? {test_file.is_file()}")

# Check if it's a directory
print(f"Is it a directory? {test_file.is_dir()}")

# Check if path is absolute
print(f"Is absolute path? {test_file.is_absolute()}")

# ===== FILE OPERATIONS =====
print("\n--- File Operations ---")

# Read entire file as text
content = test_file.read_text()
print(f"File content: {content}")

# Write text to a file
new_file = script_dir / "new_demo.txt"
new_file.write_text("Hello, World!\nThis file was created with write_text().")
print(f"Created new file: {new_file.name}")

# Create a directory
test_dir = script_dir / "test_directory"
test_dir.mkdir(exist_ok=True)
print(f"Created directory: {test_dir.name}")

# Create nested directories
nested_dir = script_dir / "data" / "input" / "files"
nested_dir.mkdir(parents=True, exist_ok=True)
print(f"Created nested directories: {nested_dir}")

# List items in directory using iterdir()
print("\nFiles in script directory using iterdir():")
for item in script_dir.iterdir():
    if item.name.startswith("test_") or item.name.startswith("new_"):
        print(f"  - {item.name} (is_file: {item.is_file()})")

# Search for files using glob()
print("\nAll .txt files in script directory using glob():")
for txt_file in script_dir.glob("*.txt"):
    print(f"  - {txt_file.name}")


# ===== PRACTICAL EXAMPLE =====
print("\n--- Practical Example: List all Python files ---")

# Find all Python files in the script directory
python_files = list(script_dir.glob("*.py"))

print(f"Python files in {script_dir.name}:")
for py_file in python_files[:5]:  # Show first 5 files
    size = py_file.stat().st_size
    print(f"  - {py_file.name}: {size} bytes")

if len(python_files) > 5:
    print(f"  ... and {len(python_files) - 5} more files")

# ===== CLEANUP =====
print("\n--- Cleanup ---")

# Delete files
for file_to_delete in [test_file, new_file, dest_copy, final_dest]:
    if file_to_delete.exists():
        file_to_delete.unlink()
        print(f"Deleted: {file_to_delete.name}")

# Delete empty directory
if test_dir.exists():
    test_dir.rmdir()
    print(f"Deleted empty directory: {test_dir.name}")

# Delete nested directories (recursively)
if nested_dir.exists():
    shutil.rmtree(nested_dir.parent.parent)
    print(f"Deleted nested directories recursively")

print("\n" + "=" * 60)
print("DEMONSTRATION COMPLETE")
print("=" * 60)