import sys

if len(sys.argv) == 3:
    answer = 0
    target = sys.argv[1]
    sentence = sys.argv[2]
    word_list = sentence.split()
    for i in word_list:
        if target == i:
            answer += 1
    print(answer)
else:
    print("none")