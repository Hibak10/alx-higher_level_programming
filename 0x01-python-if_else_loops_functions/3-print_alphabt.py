#!/usr/bin/python3
i = 97
for i in range(97, 123):
    if i == 113 or i == 101:
        continue
    print("{:c}".format(i), end="")
