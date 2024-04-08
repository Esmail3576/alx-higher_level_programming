#!/usr/bin/python3
if __name__ == "__main__":
    import marshal
with open("hidden_4.pyc", 'r') as hid:
    hidden = marshal.load(hid)
dir(hidden)
