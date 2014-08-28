#!/usr/bin/env python 

def search(sequence,number,lower=0,upper=None) :
    print "--------"
    if upper  is None :
        upper=len(sequence)-1
    if lower == upper :
        assert number == sequence[upper]
        return upper
    else :
        middle = (lower+upper) // 2
        if number > sequence[middle]:
            return search(sequence,number,middle+1,upper)
        elif number == sequence[middle] :
            return middle
        else :
            return search(sequence,number,lower,middle-1)
