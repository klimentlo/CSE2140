# b_calculator.py

'''
title: simple calculator
author: Kliment Lo
date-created: 0/80/9/2022
'''

while True:
    '''
    "while" is a conditional statement. Conditional statements separates parts of the program code so that a portion of the code is run only when a specific condition is met ("while True" means the condition IS met). The conditions must be True or False statements which determine whether the True or False code blocks are run (False blocks often follow else:)
    '''
    # -- INPUTS -- #
    NUMBER1 = input ("Please enter the first number. ")
    '''
    Sets the variable INPUT1 to the string that the user enters when responding to the prompt " Please enter the first number"
    '''
    OPERATION = input ("Choose an operation: (+, -, *, /) ")
    NUMBER2 = input ("Please enter the second number. ")

    # -- PROCESSING -- #
    NUMBER1 = int(NUMBER1)
    NUMBER2 = int(NUMBER2)
    if OPERATION == "/":
        if NUMBER2 == 0:
            print("You can't divide by 0! ")
            NUMBER2 = input("Enter a divisor that is not zero ")
            NUMBER2 = int(NUMBER2)
    '''
    Changes the variables NUMBER 1 and NUMBER 2 from their current data type (in this case, a string) to an integer
    
    This allows us to perform calculations with the variables
    '''

    if OPERATION == "+":
        RESULT = NUMBER1 + NUMBER2
    else:
        if OPERATION == "-":
            RESULT = NUMBER1 - NUMBER2
        else:
            if OPERATION == "*":
                RESULT = NUMBER1 * NUMBER2
            else:
                if OPERATION == "/":
                    RESULT = NUMBER1 / NUMBER2
                else:
                    print ("Please enter +, -, *, /, for your operation")
                    continue
    # -- OUTPUTS -- #
    print("The answer is " + str(RESULT) + "." )

    # -- INPUTS -- #
    AGAIN = input ("Perform another calculation? (y/n)")

    # -- PROCESSING -- #
    if AGAIN == "n":
        print("Why would you leave me ? Please, come back. First my dad, then my mom, and my friend. Not you too. Please don't go, not again. :'(")