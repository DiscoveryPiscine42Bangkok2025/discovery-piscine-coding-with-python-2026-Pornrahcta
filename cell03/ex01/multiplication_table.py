print("Enter a number")
user_input = input()
try:
    number = int(user_input)
    for i in range(10):
        print(f"{i} x {number} = {i*number}")
except:
    print("Input is not a number.")