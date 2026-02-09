user_input = input("Please tell me your age: ")
try:
    number = int(user_input)
    print(f"You are currently {number} years old.")
    for i in range(1,4):
        i *= 10
        print(f"In {i} years, you'll be {number + i} years old.")
except:
    print("Input is not number.")