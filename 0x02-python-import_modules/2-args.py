#!/usr/bin/python3
if __name__ == "__main__":
    import sys
number = 0
for arg in sys.argv:
    if number == 0:
        if len(sys.argv) > 2:
            print("{} arguments:".format(len(sys.argv) - 1))
        elif len(sys.argv) == 2:
            print("1 argument:")
        else:
            print("0 arguments.")
    elif number > 1:
        print("{}: {}".format(number, arg))
    else:
        print("{}: {}".format(number, arg))
    number += 1
