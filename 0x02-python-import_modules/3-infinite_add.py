#!/usr/bin/python3
if __name__ == "__main__":
    import sys
index = 0
result = 0
for arg in sys.argv:
    if len(sys.argv) == 1:
        result = 0
    elif index > 0:
        number = int(arg)
        result += number
    index += 1

print("{}".format(result))
