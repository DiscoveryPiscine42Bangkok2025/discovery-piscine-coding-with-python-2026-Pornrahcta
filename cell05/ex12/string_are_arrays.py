import sys

if len(sys.argv) == 2:
    sentence = sys.argv[1]
    z = ""
    for i in sentence:
        if i == "z":
            z += "z"
    if z:
        print(z)
    else:
        print("none")
else:
    print("none")