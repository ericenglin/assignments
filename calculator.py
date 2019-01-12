#!/usr/bin/env python3


#Write a program that defines four functions 
#(multiply, add, subtract, and divide). 
#These functions should not print anything, 
#they should simply perform a mathematical 
#operation on the two arguments and return 
#the value.

def multiply(a,b):
	return a*b

def add(a,b):
	return a+b

def subract(a,b):
	return a-b

def divide(a,b):
	return a/b



print("I'm going use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)



#bonus

#Add two more functions, square and cube.
#Make a function called square_n_times that 
#takes two arguments, number and n. square 
#the number n times and return the result.


def square(a):
	a*a

def cube(a):
	a**3

def square_n_times(a,b):
	a**b





