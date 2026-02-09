import sys

def shrink(word):
    character = word[:8]
    return character

def enlarge(word):
    size = 8
    if len(word) < 8:
        for i in range(size - len(word)):
            word += "Z"
    return word

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        if len(i) > 8:
            print(shrink(i))
        elif len(i) < 8:
            print(enlarge(i))
        else:
            print(i)
else:
    print("none")