# File Handling Tasks in Python

This project demonstrates basic file handling operations in Python through two simple tasks:

---

## 🧾 Task 1: Read from a File with Error Handling

This script attempts to read content from a file named `sample1.txt`. If the file does not exist, it handles the `FileNotFoundError` and displays an appropriate message.

### 📄 Code

```python
filename = 'sample1.txt'

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
```

### ✅ Sample Output

If file exists:
```
<contents of sample1.txt>
```

If file does not exist:
```
File 'sample1.txt' not found.
```

---

## 📝 Task 2: Write, Append, and Read File

This script:
1. Takes input from the user and writes it to `output.txt`
2. Appends more data to the same file
3. Reads and displays the full content of the file

### 📄 Code

```python
input_data = input("Enter text to write to the file: ")

with open('output.txt', "w") as file:
    file.write(input_data + '\n')

print('Data successfully written to output.txt')

additional_data = input("Please enter your additional input: ")
with open('output.txt', "a") as file:
    file.write(additional_data + '\n')

try:
    with open('output.txt', "r") as file:
        content = file.read()
        print("\n Final Content of 'output.txt':")
        print(content)
except FileNotFoundError:
    print("File 'output.txt' not found.")
```

### ✅ Sample Flow

```
Enter text to write to the file: Hello
Data successfully written to output.txt
Please enter your additional input: World

Final Content of 'output.txt':
Hello
World
```

---

## 🛠 Requirements

- Python 3.x
- No external libraries required

---

## 📚 License

Free for educational use.