input_data= input("Enter text to write to the file: ")

with open('output.txt', "w") as file:
    file.write(input_data + '\n')

print('Data successfully written to output.txt')

additional_data = input("Please enter your additional input: ")
with open('output.txt', "a") as file:
    file.write(additional_data + '\n')

try:
    with open('output.txt', "r") as file:
        content= file.read()
        print("\n Final Content of 'output.txt':'")
        print(content)
except FileNotFoundError:
    print("File 'output.txt' not found.")