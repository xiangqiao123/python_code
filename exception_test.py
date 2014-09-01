#!/usr/bin/env python

try :
    x = input("Enter the first number:")
    y = input("Enter the second number:")
    print x / y
except ZeroDivisionError :
    print "the second number can not be zero "
except TypeError :
    print "That was not a number ,was it?"
