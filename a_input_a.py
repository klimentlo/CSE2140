# a_variables_inputs.py
'''
title: Computing Science 10 Review
author: Kliment Lo
date-created: September 7,2022
'''

# --- VARIABLES --- #

STRING = "7"
# surrounding text with quotation marks denotes that it is a string
INTEGER = 7
# a number without a decimal and without quotation marks wil be an integer
FLOAT = 7.0

print (STRING)
print (INTEGER)
print (FLOAT)

### --- Typecasting --- ###
'''
a numeric string can be typecast to an integer or a float to perform calculations
'''

NEWSTRING = "9"
INTRING = int(NEWSTRING)
FLOATSTRING = float(NEWSTRING)

#print(INTSTRING)
#print(FLOATSTRING)

## -- Inputs and Conditional Statements -- ##
USER_INPUT = input("Please enter a number.")
# input ALWAYS stores data as a string
print(USER_INPUT)
#this will print a string
USER_INPUT = int(USER_INPUT)
if USER_INPUT > 32:
   print("Woah that's a big meatball")
else:
   print("That number is way too small, i can't count that low :(")