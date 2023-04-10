#!/bin/bash

/usr/bin/wget -A.txt $URL -O qso.raw

chmod +x exec/collect.py && exec/collect.py

rm qso.raw

yarn && yarn build