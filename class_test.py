#!/usr/bin/env python

class Person :
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello World ! I'm  %s." %self.name
