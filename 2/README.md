# 🐍 Python Tasks: Conditional & Loop-Based Operations

This project includes two beginner-friendly Python programs focusing on conditionals and loops.

---

## ✅ Task 1: Even or Odd Checker

### 📋 Description:
This program prompts the user to enter a number, checks whether it's even or odd, and displays the result.

### 💡 Features:
- Accepts a single integer input
- Uses the modulo operator to determine parity
- Outputs whether the number is even or odd

### 🧪 Sample Input/Output:
```
Enter a number..7
num is odd
```

### 🛠️ Code:
```python
num = int(input('Enter a number..'))

if num % 2 == 0:
    print('num is even')
else:
    print('num is odd')
```

---

## ✅ Task 2: Sum of Numbers from 1 to 49

### 📋 Description:
This program uses a `for` loop to calculate the sum of all numbers from 1 to 49.

### 💡 Features:
- Demonstrates use of a `for` loop
- Accumulates the sum using a loop variable
- Outputs the final result

### 🧪 Output:
```
addition 1225
```

### 🛠️ Code:
```python
sum = 0

for i in range(1, 50):
    sum += i

print('addition', sum)
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

- Add input validation to check if the input is an integer.
- Let the user define the range in Task 2.
- Handle edge cases like negative input in Task 1.

---