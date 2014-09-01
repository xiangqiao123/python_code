#!/usr/bin/env python

__metaclass__ = type

class Bird :
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry == True :
            print "Aaaah..."
            self.hungry=False
        else :
            print "No thanks!"

class SongBird(Bird):
    def __init__(self) :
        super(SongBird,self).__init__()
        self.sound="ssdfas"
    def sing(self):
        print self.sound
