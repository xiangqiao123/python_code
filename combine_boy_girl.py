#!/usr/bin/env python

boys=["ace","bvf","efg"]
girls=["acl","eftg","tgh"]

dic_girls={}

for girl in girls :
    dic_girls.setdefault(girl[0],[]).append(girl)

#print dic_girls
#print [ b for b in boys ]
print [ b +"+"+ g  for b in boys  if b[0] in dic_girls for g in dic_girls.get(b[0])]
