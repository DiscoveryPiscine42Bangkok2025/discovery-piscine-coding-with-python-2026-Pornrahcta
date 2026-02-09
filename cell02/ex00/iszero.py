user_input =  input()
try:
    number = int(user_input)
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except:
    print("Input is not a number.")