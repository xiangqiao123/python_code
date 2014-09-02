#!/usr/bin/env python 

import shelve

def store_person(db):
    pid = raw_input("ID:")
    person= {}
    person['name']=raw_input("name:")
    person['age']=raw_input("age:")
    person["phone"]=raw_input("phone:")
    
    db[pid]=person


def lookup_person(db):
    pid=raw_input("ID:")
    field=raw_input("field(name,age,phone):")
    field=field.strip().lower()
    print field.capitalize() + ":" +db[pid][field]

def print_help():
    print "the available commands are :"
    print "store"
    print "lookup"
    print "quit"
    


def enter_command():
    cmd=raw_input("cmd:")
    cmd=cmd.strip().lower()
    return cmd

def main():
    database=shelve.open("database.dat")
    try:
        while True:
                       cmd=enter_command()
                       if cmd == "store":
                              store_person(database)
                       elif cmd == "lookup" :
                              lookup_person(database)
                       elif cmd == "?":
                              print_help()
                       elif cmd == "quit" :
                              return 
    finally:
        database.close()


if __name__=="__main__":
    main()

