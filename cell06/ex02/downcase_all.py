import sys

def downcase_it(word):
    lower_word = word.lower()
    return lower_word

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        print(downcase_it(i))

else:
    print("none")