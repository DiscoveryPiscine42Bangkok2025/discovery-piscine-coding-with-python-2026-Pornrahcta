import sys

if len(sys.argv) == 2:
    word = sys.argv[1]
    user_input = input("What was the parameter? ")
    if user_input == word:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")