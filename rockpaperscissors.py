#!/usr/bin/env python3
""" Rock Paper Scissors Game | VArmstrong"""
import random

#user must make a choice
#must import "random" module
#computer must make a choice (randomly)
#choices must be evaluated
#print out result (who won?)

def main ():
    """body of the game"""
   
    print("Welcome to Rock Paper Scissors!")
    
    choice= input("Choose Rock, Paper, or Scissors! \n>")
    
    choice= choice.lower()
    
    if choice in ["Rock", "Paper", "Scissors"]:
        print("success!!")

main()

