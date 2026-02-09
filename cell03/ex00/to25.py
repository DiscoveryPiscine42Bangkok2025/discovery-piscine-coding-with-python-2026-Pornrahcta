user_input = input()
try:
    number = int(user_input)
    if number > 25:
        print("Error")
    else:
        while number <= 25:
            print(f"Inside the loop, my variable is {number}")
            number += 1
except:
    print("Inside the loop, my variable is not number")