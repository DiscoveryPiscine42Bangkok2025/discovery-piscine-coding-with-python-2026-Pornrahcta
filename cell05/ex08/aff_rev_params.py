import sys

if len(sys.argv) <= 2:
    print("none")
else:
    for i in sys.argv[::-1]:
        print(i)