# file: sc_07_07_dict_in_dict.py
# Dictionary within dictionary - nested data structure example

# STUDENT DATABASE: Each student has an ID, name, and multiple course grades
# Structure: {student_id: {"name": string, "courses": {course: grade, ...}}}
grades = {
    1001: {                                    # Student ID 1001
        "name": "Paul Barnes",                 # Student's full name  
        "courses": {"math": 8, "physics": 7, "c++": 3}  # Dict of courses and grades
    },
    1031: {                                    # Student ID 1031
        "name": "Bill Shankley",
        "courses": {"math": 6, "c++": 6}       # This student only has 2 courses
    },
    1011: {                                    # Student ID 1011
        "name": "Jane Jillingham", 
        "courses": {"physics": 2, "math": 5}   # Different courses than others
    },
    1012: {                                    # Student ID 1012
        "name": "Bill Gates",
        "courses": {"java": 10, "c++": 7}      # Has Java instead of physics/math
    },
    1019: {                                    # Student ID 1019
        "name": "Jack The Ripper",
        "courses": {"math": 8, "physics": 7}   # No c++ course
    },
    1090: {                                    # Student ID 1090
        "name": "Don Henley",
        "courses": {"physics": 10, "c++": 8}   # High achiever in these subjects
    }
}

# ACCESSING NESTED DATA:
print("=== HOW TO ACCESS NESTED DICTIONARY DATA ===")
print(f"Student 1001's name: {grades[1001]['name']}")
print(f"Student 1001's math grade: {grades[1001]['courses']['math']}")
print(f"All of student 1031's courses: {grades[1031]['courses']}")

print("\n=== SAFE ACCESS WITH get() METHOD ===")
# Use get() to avoid KeyError if student or course doesn't exist
student_1001_physics = grades[1001]["courses"].get("physics", "Not taken")
student_1012_physics = grades[1012]["courses"].get("physics", "Not taken")  
print(f"Student 1001 physics grade: {student_1001_physics}")
print(f"Student 1012 physics grade: {student_1012_physics}")

def get_grades(item):
    """Calculate total of physics and c++ grades for sorting
    
    Args:
        item: A tuple of (student_id, student_info_dict) from grades.items()
    
    Returns:
        int: Sum of physics and c++ grades (0 if course not taken)
    """
    courses = item[1]["courses"]  # Get the courses dict from student info
    physics_grade = courses.get("physics", 0)  # 0 if not taking physics
    cpp_grade = courses.get("c++", 0)          # 0 if not taking c++
    return physics_grade + cpp_grade

print("\n=== SORTING BY CALCULATED VALUES ===")
# Sort students by their physics + c++ grades (highest first)
sorted_list = sorted(grades.items(), key=get_grades, reverse=True)
sorted_dict = dict(sorted_list)

# Display sorted results
for student_id, info in sorted_dict.items():
    name = info["name"]
    physics = info["courses"].get("physics", 0)
    cpp = info["courses"].get("c++", 0) 
    total = physics + cpp
    print(f"ID {student_id}: {name:20} - Physics: {physics}, C++: {cpp}, Total: {total}")

print("\n=== PEDAGOGICAL BREAKDOWN ===")
print("""
This grades dictionary demonstrates THREE levels of nesting:

LEVEL 1: Student IDs (1001, 1031, etc.)
    - These are the main keys
    - Each represents a unique student

LEVEL 2: Student Information ("name" and "courses") 
    - Each student has exactly two attributes:
      * "name": a simple string with the student's name
      * "courses": another dictionary containing their grades

LEVEL 3: Individual Course Grades ("math", "physics", "c++", "java")
    - The innermost level contains subject-grade pairs
    - Grades are integers from 0-10
    - Not all students take the same courses

ACCESSING PATTERNS:
1. Get student name:     grades[student_id]["name"]
2. Get specific grade:   grades[student_id]["courses"]["subject"]
3. Get all courses:      grades[student_id]["courses"]
4. Safe access:          grades[student_id]["courses"].get("subject", 0)

EDUCATIONAL VALUE:
- Shows real-world data organization (students, courses, grades)
- Demonstrates when simple lists/dictionaries aren't enough  
- Teaches safe access patterns with get() method
- Illustrates sorting by computed values from nested data
""")

# Example of iterating through the entire structure
print("\n=== COMPLETE DATA OVERVIEW ===")
for student_id, student_info in grades.items():
    print(f"\nStudent {student_id}: {student_info['name']}")
    for course, grade in student_info["courses"].items():
        print(f"  {course}: {grade}")

# Sorter etter sum av physics og c++
sorted_list = sorted(grades.items(), key=get_grades, reverse=True)
sorted_dict = dict(sorted_list)

print("Sorted by sum of physics and c++ grades:")
for student_id, info in sorted_dict.items():
    print(f"{student_id}: {info['name']}, Courses: {info['courses']}")
