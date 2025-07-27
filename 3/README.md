# Python Math Operations

This repository contains two Python scripts that demonstrate basic mathematical operations using built-in functions and the `math` module.

---

## 🧮 Task 1: Factorial Calculation

This script calculates the **factorial** of a given non-negative integer using a **recursive function**.

### 📌 Description

- Prompts the user to enter a number
- Uses a recursive function to calculate the factorial
- Outputs the result to the console

### 📄 Code

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input('Enter a number for which you want to calculate the factorial: '))
print(factorial(number))
```

### ✅ Sample Output

```bash
Enter a number for which you want to calculate the factorial: 5
120
```

---

## 📊 Task 2: Square Root, Logarithm, and Sine

This script performs the following mathematical operations:

- **Square root**
- **Natural logarithm (base _e_)**
- **Sine** (in radians)

### 📌 Description

- Prompts the user to enter a positive number
- Uses the `math` module to compute:
  - Square root with `math.sqrt()`
  - Natural logarithm with `math.log()`
  - Sine with `math.sin()` (expects radians)
- Prints the results to the console

### 📄 Code

```python
import math

number = int(input('Enter a number '))

sqaureRoot = math.sqrt(number)
mathLogRoot = math.log(number)
mathSin = math.sin(number)

print('Square root ', sqaureRoot)
print('Logarithm ', mathLogRoot)
print('Sine ', mathSin)
```

### ✅ Sample Output

```bash
Enter a number: 10
Square root  3.1622776601683795
Logarithm  2.302585092994046
Sine  -0.5440211108893698
```

---

## ⚠️ Notes

- Task 1 assumes a **non-negative integer** as input for factorial.
- Task 2 assumes the input number is **positive** (logarithm and square root are undefined for negative numbers in the real number system).
- The sine function uses the input as **radians**, not degrees. Use `math.radians(degrees)` if you need to convert from degrees.

---

## 🚀 How to Run

1. Save the scripts in separate files (e.g., `task1.py` and `task2.py`)
2. Run them from your terminal:

```bash
python task1.py
python task2.py
```

---

## ✅ Requirements

- Python 3.x
- No external libraries needed (uses standard `math` module)

---

## 📚 License

This project is open for educational and personal use.