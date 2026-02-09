import sys

if len(sys.argv) == 3:
    try:
        lower_limit = int(sys.argv[1])
        upper_limit = int(sys.argv[2])
        array_list = []
        if lower_limit > upper_limit:
            temp = lower_limit
            lower_limit = upper_limit
            upper_limit = temp
        for i in range(lower_limit,upper_limit + 1):
            array_list.append(i)
        print(array_list)
    except:
        print("Input is not a number.")
else:
    print("none")