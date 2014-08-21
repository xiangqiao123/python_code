#!/usr/bin/env python

database=[
    ["a","123"],
    ["b","1234"],
    ["c","134"],
    ["d","234"]
]

username=raw_input("input your name:")
pin=raw_input("input your pin:")

if [username,pin] in database:
   print "Access granted"
