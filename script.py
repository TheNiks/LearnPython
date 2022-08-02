# Start new journey 2-Aug
import string


print("Hello World")

myint = 7
print(myint)

name = "nikunj"
print(name.upper())

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a,b = 3,4
print(a,b)

# Mixing operators are not supported
# print(one + two + hello)

#Exercise
"""The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". 
The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20."""

mystring = "hello"
myfloat = 10.0
myint = 20

#testing Code
if mystring == "hello":
    print("String: %s" %mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20 :
    print("Int: %d" % myint)




