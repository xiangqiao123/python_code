#!/usr/bin/env python

class Secretive:
    def __inaccessible(self) :
        print "Bet you can nit see me ..."
    def accessible(self):
        print "The secret message is :"
        self.__inaccessible()
