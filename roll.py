# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import random
# question1 = input("How many dices[0-3]?")
question2 = input('Would you like to roll the dice[y/n]?')

while question2 != 'n':
    if question2 == 'y':
        question1 = input('How many dices[1-3]?')
        if question1 == '1':
            die1 = random.randint(1,6)
            print(die1)
            question2 = input('Would you like to roll the dice[y/n]?')
        elif question1 == '2':
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(die1,die2)
            question2 = input('Would you like to roll the dice[y/n]?')
        elif question1 == '3':
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            die3 = random.randint(1,6)
            print(die1, die2,die3)
            question2 = input('Would you like to roll the dice[y/n]?')
        else:
            print("Error")
            question2 = input('Would you like to roll the dice[y/n]?')
    else:
        print('Invalid response. Please type "y" or "n".')
        question2 = input('Would you like to roll the dice[y/n]?')

print('Good-bye!')