#!/usr/bin/env python3

import random
import time

# computer needs to make a choice
# choices need to be evaluated
# print out the result (who won)


print("Welcome to the game!")

def main():
    """body of the game"""

    time.sleep(1)
    choice= input("Make a choice: Rock, Paper, or Scissors?\n>")
    time.sleep(1)
    botchoice= random.choice(["rock", "paper", "scissors"])
    time.sleep(1)

    choice= choice.lower() # validates input by forcing input to be lower case

    # uncomment these print functions to debug
    print(f"You chose {choice}!")
    time.sleep(.5)
    print(f"Python chose {botchoice}!")
    time.sleep(.5)
    if choice not in ["rock", "paper", "scissors"]:
        print("You entered an invalid choice, you lose(r)!")
        main()
    elif choice == "scissors" and botchoice == "paper":
        print("Scissors beats Paper! You win!")
    
    elif choice == "rock" and botchoice == "scissors":
        print("Rock beats Scissors! You win!")
    
    elif choice == "paper" and botchoice == "rock":
        print("Paper beats Rock! You win!")
    
    elif choice == "rock" and botchoice == "paper":
        print("Paper beats rock! You lose(r)!")
    
    elif choice == "scissors" and botchoice == "rock":
        print("Rock beats Scissors! You lose(r)!")    

    elif choice == "paper" and botchoice == "scissors":
        print("Scissors beats Paper! You lose(r)!")
    
    elif choice == "scissors" and botchoice == "scissors":
        print("Tie game!")
    
    elif choice == "rock" and botchoice == "rock":
        print("Tie game!")
    
    elif choice == "paper" and botchoice == "paper":
        print("Tie game!")
    time.sleep(1)
    print("Thanks for playing!")
    again= input("Play again? Y/N: \n>")
    
    again= again.lower()
    if again not in ["n", "y"]:
        print ("invalid choice, quitting!")
    
    again= again.lower()
    if again == "y":
        main()
    
    if again == "n":
        print("have a nice day!")
# user picked scissors... did they win or lose?

    ### ADD MORE HERE

main()
