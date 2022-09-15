# c_magic_8_ball.py

'''
title: magic 8 ball
authpr: Thomas patterspm
date-created: 2022-12-09
'''

import random

#random is the library name that lets us chose a random integer using the command randint


# --- INPUTS --- #
# user asks a question (define a variable and record it as a string input like the calculator program
QUESTION = input("What must you wish to know? ")

# --- PROCESSING --- #
if QUESTION != "":
    ANSWER= random.randint(1,20)
else:
    QUESTION != input ("You must ask a question to gain my knowledge. What do you wish to know?")
    ANSWER = random.randint(1,20)
#random.randit(1,20) uses the randint command from the random library to create an integer with a random value from 1-20
#if QUESTION != "" will be True if QUESTION contains text and is not an empty string ("" represent an empty string)


# --- OUTPUTS --- #
#give a response based on the random integer
if ANSWER == 1:
    print("Yea, don't worry bout it")
elif ANSWER == 2:
    print ("Probably lmao")
elif ANSWER == 3:
    print ("Without a doubt idiot")
elif ANSWER == 4:
    print("Oh yea for sure")
elif ANSWER == 5:
    print("Trust me, it'll be fine")
elif ANSWER == 6:
    print("yeeeeeSSSSS")
elif ANSWER == 7:
    print("YESSIRRRR    ")
elif ANSWER == 8:
    print("Please do it")
elif ANSWER == 9:
    print("Do it, it's gonna go great")
elif ANSWER == 10:
    print("SI SI SI.")
elif ANSWER == 11:
    print("My guy, I didn't understand ANY of that. ")
elif ANSWER == 12:
    print("Reword that, your grammar sucks $%#% ")
elif ANSWER == 13:
    print("Give me a minute, me think. ")
elif ANSWER == 14:
    print("Bro what? say that again?")
elif ANSWER == 15:
    print("It is decidedly so.")
elif ANSWER == 16:
    print("nah fam don't do it :skull emoji: ")
elif ANSWER == 17:
    print("no. ")
elif ANSWER == 18:
    print("Don't do it ")
elif ANSWER == 19:
    print("I doubt it, go next ")
else:
    print("Tf you on???? Hell nah I don't believe it fam ")
