#!/usr/bin/env python

import sys
from vonny import vonnytize
try:
    print(vonnytize(sys.argv[1]))
except IndexError:
    print('Say me wht i shld vnnytze')
exit(0)
