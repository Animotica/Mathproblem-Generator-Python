import random
from os import name, system
from time import sleep
from string import digits

correcte = []
trys = []

def clear(): #can clear the console !But only on windows!
    system('cls')

def start():
    clear()
    # Is like a 'menu/main menu'
    print("For simple math press 's'")
    print("For hardcore math enter 'm'")
    choic = input()

    if choic == 's':
        clear()
        game()

    elif choic == 'm':
        clear()
        midgame()

    else:
        print("Invalid Input. Press any key to return...")
        input()
        start()

def game():
    print("Please hang on... \n-----------------------\nGenerating new Mathproblem...")
    sleep(3)
    clear() # clears console

#- In the next few lines it will calculate the percent of the correct inputs! -#
    a = correcte.count('a')
    b = trys.count('a')

    #- -#
    global percent_
    percent_ = 0

    if b == 0:
        pass

    else:
        percent_ = 100 / b
        percent_ = percent_ * a
        percent_ = int(percent_)

    a = str(a)
    b = str(b)
    percent = str(percent_)

    print(a + " out of " + b + " problems correct.  (" + percent + "%)")

# generates some stuff to calculate (Simpler Version of the Mathproblem generator)
    a = random.choice(['+', '-', '*'])
    print("Mathproblem succesfully created: ")
    if a == '+':
        a = list(range(1, 101))
        x = random.choice(a)
        b = list(range(1, 101))
        y = random.choice(a)
        print(str(x) + " + " + str(y))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        result = x + y
        user = input()
        if int(user) == result:
            correct()

        else:
            incorrect()

    if a == '-':
        a = list(range(1, 101))
        x = random.choice(a)
        b = list(range(1, 101))
        y = random.choice(a)
        print(str(x) + " - " + str(y))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        result = x - y
        user = input()
        if int(user) == result:
            correct()

        else:
            incorrect()

    if a == '*':
        a = list(range(-15, 15))
        x = random.choice(a)
        b = list(range(-15, 15))
        y = random.choice(a)
        print(str(x) + " * " + str(y))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        result = x * y
        user = input()
        if int(user) == result:
            correct()

        else:
            incorrect()

# Gives the opinion of choosing the next steps and also displays if somthing has been enter correct/incorrect
def correct():
    print("Correct...")
    print("-------------------------------------------------")
    print("Press 'q' to quit, 'm' to enter the start menu or ANY other key to return...")
    b = input("waiting for input: ")
    if b == 'q':
        quit()
    elif b == 'm':
        start()
    else:
        corr1()

def incorrect():
    print("Incorrect...")
    print("-------------------------------------------------")
    print("Press 'q' to quit, 'm' to enter the start menu or ANY other key to return...")
    b = input("waiting for input: ")
    if b == 'q':
        quit()
    elif b == 'm':
        start()
    else:
        adding1()

def midgame():
    print("Please hang on... \n-----------------------\nGenerating new Mathproblem...")
    sleep(3)
    clear()

# Shows how many of your trys you have correct
    a = correcte.count('a')
    b = trys.count('a')

    #- In the next few lines it will calculate the percent of the correct inputs! -#
    global percent_
    percent_ = 0

    if b == 0:
        pass

    else:
        percent_ = 100 / b
        percent_ = percent_ * a
        percent_ = int(percent_)

    a = str(a)
    b = str(b)
    percent_ = str(percent_)

    print(a + " out of " + b + " problems correct. (" + percent_ + "%)")
    print("Mathproblem succesfully created: ")

# generates some numbers to calculate (Harder Version of the Mathproblem generator)
    a = random.choice(['+', '-', '*'])
    if a == '+':
        a = list(range(-1001, 1001))
        x = random.choice(a)
        b = list(range(-1001, 1001))
        y = random.choice(a)
        print(str(x) + " + " + str(y))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        result = x + y
        user = input()
        if int(user) == result:
            mcorrect()

        else:
            mincorrect()

    if a == '-':
        a = list(range(-1001, 1001))
        x = random.choice(a)
        b = list(range(-1001, 1001))
        y = random.choice(a)
        print(str(x) + " - " + str(y))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        result = x - y
        user = input()
        if int(user) == result:
            mcorrect()

        else:
            mincorrect()

    if a == '*':
        a = list(range(-100, 100))
        x = random.choice(a)
        b = list(range(-150, 150))
        y = random.choice(a)
        print(str(x) + " * " + str(y))
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        result = x * y
        user = input()
        if int(user) == result:
            mcorrect()

        else:
            mincorrect()

# Gives the opinion of choosing the next steps and also displays if somthing has been enter correct/incorrect
def mcorrect():
    print("Correct...")
    print("-------------------------------------------------")
    print("Press 'q' to quit, 'm' to enter the start menu or ANY other key to return...")
    b = input("waiting for input: ")
    if b == 'q':
        quit()
    elif b == 'm':
        start()
    else:
        corr2()

def mincorrect():
    print("Incorrect...")
    print("-------------------------------------------------")
    print("Press 'q' to quit, 'm' to enter the start menu or ANY other key to return...")
    b = input("waiting for input: ")
    if b == 'q':
        quit()
    elif b == 'm':
        start()
    else:
        adding2()

#- Scoring how many points out of trys someone has -#

def adding1():
    trys.append('a')
    game()

def adding2():
    trys.append('a')
    midgame()

def corr1():
    correcte.append('a')
    trys.append('a')
    game()

def corr2():
    correcte.append('a')
    trys.append('a')
    midgame()
clear()
start()

#This Idea came from a friend who made this in c# while I did it in Python. So have fun while trying it.
