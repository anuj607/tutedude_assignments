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