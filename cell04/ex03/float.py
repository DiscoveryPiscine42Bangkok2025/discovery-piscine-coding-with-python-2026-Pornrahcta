try:
    number = float(input("Give me a number: "))
    if number == int(number):
        print("This number is a integer.")
    else:
        print("This number is an decimal.")
except:
    print("Input is not a number")