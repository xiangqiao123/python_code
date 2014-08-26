#!/usr/bin/env python

import math
for i in range(99,0,-1) :
    print "test",i
    temp = math.sqrt(i)
    if temp == int(temp):
        print "ok",i
        break
