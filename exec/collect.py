#!/usr/bin/python3

import os
import re
import json


def main():
    j = []
    with open("qso.raw") as f:
        t = f.read()
    reg = r'<CALL:\d+>(\w{3,6})\r?\n<BAND:\d+>(\w+)\r?\n<FREQ:\d+>(\S+)\r?\n<MODE:\d+>(\S+)\r?\n(?:<.*>.*\r?\n)*<APP_LoTW_QSO_TIMESTAMP:\d+>(\S+) //.*\r?\n(?:<.*>.*\r?\n)*<QSL_RCVD:1>(\w)\r?\n(?:<.*>.*\r?\n)*<eor>'
    regc = re.compile(reg, re.MULTILINE)
    m = regc.findall(t)
    print("Found {} records.".format(len(m)))
    with open("src/data/qso.json", "w") as f:
        json.dump(m, f)


main()
