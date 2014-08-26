#!/usr/bin/env python 

names = ["dog","cat","fish","bird"]
ages= [32,21,23,3]
'''
for i in range(len(names)) :
    print names[i],ages[i]
'''

for k,v in zip(names,ages) :
    print k,",",v
