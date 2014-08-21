#!/usr/bin/env python

people={
       "xiangqiao":
        {
           "phone":"152025",
           "addr":"TJ"
        },
       "xiaoming":
       {
           "phone":"155645",
           "addr":"BJ"
       },
       "baidu":
       {
           "phone":"010",
           "addr":"BeiJin"
       }

}

name=raw_input("input name:")
request=raw_input("input request(phone=p,addr=a):")

if request=='p':
    key="phone"
if request=='a':
    key="addr"

if name in people :
    print "%s's %s is %s" %(name,key,people[name][key])

