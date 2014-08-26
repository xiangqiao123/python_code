#!/usr/bin/env python

str = ["qw","qwer","ww","wwer"]

for i,v in enumerate(str) :
   #print i,v
   if "ww" in v :
        str[i]="del"

print str
