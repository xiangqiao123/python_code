#!/usr/bin/env  python
def fib(num) :
    'calculate fibs array'
    fibs=[0,1]
    #num=input("please input the number:")
    for i in range(num-2) :
        fibs.append(fibs[-2]+fibs[-1])
 
    return fibs

#num=input("please input the number:")
#print fib(num)
