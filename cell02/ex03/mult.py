print("Enter the first number:")
first_input = input()
print("Enter the second number")
second_input = input()
try:
    first_number = int(first_input)
    second_number = int(second_input)
    answer = first_number * second_number
    print(f"{first_input} x {second_input} = {answer}")
    if answer < 0:
        print("This number is negative.")
    elif answer > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except:
    print("Input is not a number.")