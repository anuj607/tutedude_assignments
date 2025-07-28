# 📘 Python Dictionary and List Operations

## ✅ Task 1: Student Marks Lookup

This task creates a dictionary where student names are keys and their marks are values. It takes a student's name as input and returns their mark if found, otherwise displays a "not found" message.

### 🔹 Code:
```python
student_marks = {
    "a": 85,
    "b": 92,
    "c": 78,
    "d": 90
}
name = input("Press enter student name ")

if name in student_marks:
    mark = student_marks[name]
    print(f"{name}'s mark is {mark}")
else:
    print(f"student '{name}' not found in the dictionary.")
```

### 🔹 Sample Output:
```
Press enter student name 
b
b's mark is 92
```

---

## ✅ Task 2: List Slicing and Reversing

This task demonstrates how to:
- Create a list of numbers from 1 to 10
- Extract the first five elements
- Reverse those five elements

### 🔹 Code:
```python
numbers = list(range(1, 11))
first_five = numbers[:5]
first_five_reversed = numbers[:5][::-1]

print(f"Original List: {numbers}")
print(f"Expected first five element: {first_five}")
print(f"Reversed extracted element: {first_five_reversed}")
```

### 🔹 Output:
```
Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected first five element: [1, 2, 3, 4, 5]
Reversed extracted element: [5, 4, 3, 2, 1]
```