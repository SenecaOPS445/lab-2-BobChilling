#!/usr/bin/env python3
# Author: Wayson Cao
# Author ID: 130300239
# Date: 2025/01/24

import sys
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

len(sys.argv)
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")