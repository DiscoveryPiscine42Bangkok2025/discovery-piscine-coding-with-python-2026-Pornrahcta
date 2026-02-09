import sys

if len(sys.argv) > 1:
    words = [i for i in sys.argv[1:] if i[-3:] != "ism"]
    if words:
        for i in words:
            print(i)
    else:
        print("none")
else:
    print("none")