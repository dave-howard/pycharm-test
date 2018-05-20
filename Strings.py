# Strings
import os

#escape char backslash \
print ('"I\'m Right", said Fred') #escsping quotes in quotes

print ("across two\nlines")

#raw string with r
print (r"all on o\ne line")

#triple quoting
print ('''text over
two lines,
or even three''')

#concatenation
a = "hello"
b = "world!"
print (a+" "+b)
print (a," ",b)
print (a,b)

a+= " everyone" # strings are immutable! this creates a new string
print (a)

c = 5 * "*" #multiply a string
print (c)

d = "01502123456"
print ("("+d[:5]+")"+d[5::]) #use slicing to get std code

name = "Dave"
age = 34

print ("%s is %d" % (name, age))
text = "{0} is {1}".format(name, age) #use strings format method
print (text)
print ("{0} is {1}".format(name, age)) #use format method as an arg to print()

print ("{} is {}".format(name, age)) #default argument ordering
#property of arg in format string
from datetime import datetime, timedelta
curr = datetime.now()
print("=>"+"hour of {0} is {0.hour}".format(curr))

#formatting a datetime into a string
print(curr.strftime("Today is %d of %B which is a %A"))

#formatting a datetime as an arg
print("Today is {0:%A}".format(curr))

#create a date from a formatted string
birthday = datetime.strptime("31/03/1975","%d/%m/%Y")
print ("{0:%A}".format(birthday))



import math
x=1
for i in range(2):
    x=x*2
    y = math.sqrt(x)
    # formatting of numbers :field-width.decimal places
    print("{0:4} {1:10} {2:10.3f}".format(i, x, y))

#split string into list
print("this is a test".split())
print(type("this is a test".split()))
print("1,2,3,4".split(","))
