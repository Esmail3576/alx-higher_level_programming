#!/usr/bin/python3
if __name__ == "__main__":
    import sys
number = 0
for arg in sys.argv:
    if number == 0:
        pass
    else:
        print("{}: {}".format(number, arg))
    number += 1
