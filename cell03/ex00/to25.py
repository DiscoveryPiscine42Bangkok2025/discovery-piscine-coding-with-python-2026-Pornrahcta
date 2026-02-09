while True:
    user_input = input()
    try:
        number = int(user_input)
        if number > 25:
            print("Error")
            break
        else:
            print(f"Inside the loop, my variable is {number}")
    except:
        print("Inside the loop, my variable is not number")