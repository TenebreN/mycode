#!/usr/bin/env python3

counter = 1
answer = " "
    
while counter < 4 and answer != "brian" and answer != "shrubbery":
        print (f"Round {counter}!")
        counter += 1
        answer= input('finish the movie title: "Monty Python\'s the Life of _____" \n>')
        
        answer= answer.lower()
        
        if answer == "brian":
            print ("Correct!")
        
        elif answer == "shrubbery":
            print("You have found the secret answer!")
        
        elif counter == 4: 
            print ("Sorry, the answer was Brian!")
        
        else:
            print ("Sorry, try again!")
