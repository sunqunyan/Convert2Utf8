#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, with_statement

import sys
from sys import argv
import getopt
import chardet

try:
    myargs = getopt.getopt(argv[1:], '', ['file='])
except getopt.GetoptError as err:
    print(str(err))
    sys.exit(2)

fname = ''
for k, v in myargs[0]:
    if k == '--file':
        fname = v
        break

try:
    f = open(fname)
except IOError as err:
    print(str(err))
    sys.exit(2)

data = f.read()
ec_info = chardet.detect(data)

try:
    cur_encode = ec_info['encoding']
except Exception as err:
    print(str(err))
    sys.exit(2)

data_decode = data.decode(cur_encode)
xx = data_decode.encode("utf-8")
tname = fname + '.utf8'
fh = open(tname, "w")
fh.write(xx)
fh.close()

print("Succeed! The new file is: " + tname)
