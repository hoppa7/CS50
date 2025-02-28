import sys


try:
    if len(sys.argv) > 2 or len(sys.argv) == 1\
        or not sys.argv[1].endswith(".py"):
        sys.exit("Please input only 1 command-line argument ending with .py")
    
    with open(sys.argv[1], "r") as file:
        line_count = 0
        for line in file:
            if not line.strip() or line.startswith("#"):
                pass
            else:
                line_count += 1

    print(line_count)
except FileNotFoundError:
    sys.exit("File not found")