# A simple calculator application.

print('''***********************************************
Welcome to my simple calculator app. 🤗\n1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
*******************************************************''')
# Addition operation

print("Enter two numbers to perform addition operation")
# Prompt user to enter first & second number and store it
first_number = input("first_number:\n>>")
second_number = input("second_number:\n>>")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum:.2f}")

# Subtraction operation

print("***************************************")
print("Subtraction")
print("Enter two numbers to perform subtraction operation")
# Prompt user to enter first & second number and store it
first_number = input("first_number:\n>>")
second_number = input("second_number:\n>>")
sub = float(first_number) - float(second_number)
print(f"{first_number} + {second_number} = {sub:.2f}")

# Multiplication operation
print("***************************************")
print("Multiplication")
print("Enter two numbers to perform multiplication operation")
# Prompt user to enter first & second number and store it
first_number = input("first_number:\n>>")
second_number = input("second_number:\n>>")
mul = float(first_number) * float(second_number)
print(f"{first_number} * {second_number} = {mul:.2f}")

# Division operation
print("***************************************")
print("Division")
print("Enter two numbers to perform division operation")
# Prompt user to enter first & second number and store it
first_number = input("first_number:\n>>")
second_number = input("second_number:\n>>")
div = float(first_number) / float(second_number)
print(f"{first_number} / {second_number} = {div:.2f}")

# Exponentiation operation
print("***************************************")
print("Exponentiation")
print("Enter two numbers to perform exponentiation operation")
# Prompt user to enter first & second number and store it
first_number = input("first_number:\n>>")
second_number = input("second_number:\n>>")
exp = float(first_number) ** float(second_number)
print(f"{first_number} ** {second_number} = {exp:.2f}")






