import sys

if len(sys.argv) > 1:
    print(f"parameters: {len(sys.argv) - 1}")
    for i in range(1,4):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
else:
    print("none")