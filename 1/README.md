# 🐍 Python Basics: User Input and Arithmetic Operations

This project contains two simple Python tasks to help beginners practice input handling, string formatting, and basic arithmetic operations.

---

## ✅ Task 1: Basic Arithmetic Calculator

### 📋 Description:
This program takes **two numbers as input** from the user, performs basic arithmetic operations (addition, subtraction, multiplication, division), and displays the results.

### 💡 Features:
- Accepts two integers as input
- Performs:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Displays the results

### 🧪 Sample Input/Output:
```
Enter the first number: 10
Enter the second number: 2
Addition 12
Subtract 8
Multiply 20
Division 5.0
```

### 🛠️ Code:
```python
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)

addition = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
division = num1 / num2

print('Addition', addition)
print('Subtract', subtract)
print('Multiply', multiply)
print('Division', division)
```

---

## ✅ Task 2: Greeting User by Name

### 📋 Description:
This program prompts the user to enter their **first and last name**, formats the input properly, and then prints a personalized greeting.

### 💡 Features:
- Trims any extra spaces
- Capitalizes the first letter of each name
- Greets the user with a full sentence

### 🧪 Sample Input/Output:
```
Enter your first name:  john
Enter your last name: doe
Hello John Doe! Welcome to the Python program.
```

### 🛠️ Code:
```python
firstname = input('Enter your first name: ').strip().title()
lastname = input('Enter your last name: ').strip().title()

print('Hello', firstname + ' ' + lastname + '!' + ' Welcome to the Python program')
```

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Save each task in its own `.py` file (e.g., `task1.py`, `task2.py`)
3. Run them from the terminal:

```bash
python3 task1.py
python3 task2.py
```

---

## 🧠 Tips for Improvement

- Add input validation (e.g., check if the input is a number).
- Handle division by zero.
- Allow the user to run multiple operations in one session.

---