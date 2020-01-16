#!/usr/bin/env python
# _*_ coding: utf-8 _*_

result = []
year = ["2017", "2018", "2019", "2020"]
with open("", "r") as f:
    count = -1
    for line in f.readlines():
        if line.strip("\n").split(" ")[-1] in year:
            result[count] += "\n"
            result.append(line.strip().strip("\n"))
            count += 1
        else:
            result[count] += " %s" % line.strip().strip("\n")

with open("result.log", "w") as f:
    f.writelines(result)
