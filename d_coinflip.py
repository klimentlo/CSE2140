#d_coinflip.py

'''
title: coin flip
author: Kliment Lo
date-created: 2022-09-12
'''

from random import randrange

#randrange is another way to generate random integer values

def intro():
    print("""
    Welcome to Coin Flip
    Get points by correctly choosing the outcome: Both heads, Both tails, or one heads and one tails.
    Lose points if you are wrong
    """)
# def intro () creates a subroutine that will run whenever we call "intro" in our program
def heads():
    print("""
     ____
    /    \\
   |  H   | 
    \\____/                         

    """)

def tails():
    print("""
     ____
    /    \\
   |  T   |
    \\____/
    """)

# --- MAIN PROGRAM CODE --- #
### ---VARIABLES --- ###
SCORE = 0
intro()
heads()
tails()
while True:
### --- INPUTS --- ###
    CHOICE = int(input("What do you think the result will be? Enter (1) for both heads, (2) for both tails or (3) for heads and tails: "))
    ### --- PROCESSING --- ###
    COIN1 = randrange(2) # randrange randomizes from 0 to a certain number based on the input range... in this case, from 0 to 1
    #for magic 8 ball, randrange(20) would randomize from 0 to 19
    COIN2 = randrange (2) # sets COIN2's value to a random integer 0 to 1

    if COIN1 == 1 and COIN2 == 1:
        RESULT = 1 #both heads
    elif COIN1 == 0 and COIN2 == 0:
        RESULT = 2 # both tails
    else:
        RESULT = 3

    ### --- OUTPUTS --- ###
    if COIN1 == 1:
        heads()
    else:
        tails()

    if COIN2 == 1:
        heads()
    else:
        tails()

    print(RESULT)
    if RESULT == CHOICE:
        print("""
Congrats! You got it correct!!!!!!!!!
        """)
        SCORE += 2
    else:
        print("""
Aw, better luck else time :(((((
        """)
        SCORE -= 1
    print("CURRENT SCORE: " + str(SCORE))
    AGAIN = input ("Would you like to continue to play? (y/n)")
    if AGAIN == "y":
        continue
    if AGAIN == "n":
        break

    if AGAIN != "y" or "n":
        print("its a yes ")
    AGAIN = input("Would you like to continue to play? (y/n)") #Thank you Judy Zhu for this line :D Permission signature: judy :(


