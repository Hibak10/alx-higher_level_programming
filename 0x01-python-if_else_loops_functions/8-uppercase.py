#!/usr/bin/python3
def uppercase(str):
    ret = ""
    for x in str:
        if ord(x) in range(97, 123):
            ret += chr(ord(x) - 32)
        else:
            ret += x
    print("{}".format(ret), end="")
    print("")
