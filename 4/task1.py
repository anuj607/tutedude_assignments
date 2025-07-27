filename='sample1.txt'

try:
    with open(filename,'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
      print(f"File '{filename}' not found.")


