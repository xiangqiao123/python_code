#!/usr/bin/env python

months=['January',
        'February',
        'March',
	'April',
	'May',
	'June',
	'July',
	'Aguest',
	'September',
	'October',
	'November',
	'December'
       ]

endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

year=raw_input("input year:")
month=raw_input("input month(1-12):")
day=raw_input("input day(1-31):")

month_name=months[int(month)-1]
day_name=day+endings[int(day)-1]

print month_name+" "+day_name+","+year
