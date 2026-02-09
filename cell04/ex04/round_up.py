import math
try:
    number = float(input("Give me a number: "))
    print(math.ceil(number))
except:
    print("Input is not a number.")