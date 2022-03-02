#!/bin/bash

/usr/bin/wget -A.txt $URL -O qso.raw

exec/collect.py

rm qso.raw

yarn && yarn build
