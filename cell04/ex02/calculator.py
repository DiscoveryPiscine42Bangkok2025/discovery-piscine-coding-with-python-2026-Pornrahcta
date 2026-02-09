first_input = input("Give me the first number: ")
second_input = input("Give me the second number: ")
try:
    print("Thank you!")
    first_number = int(first_input)
    second_number = int(second_input)
    print(f"{first_number} + {second_number} = {first_number+second_number}")
    print(f"{first_number} - {second_number} = {first_number-second_number}")
    print(f"{first_number} / {second_number} = {first_number/second_number}")
    print(f"{first_number} * {second_number} = {first_number*second_number}")
except:
    print("Input is not a number.")
