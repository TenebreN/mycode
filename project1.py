#!/usr/bin/env python3
"""what city should i live in? | VArmstrong"""

import time

Rio= 0
Montgomery= 0
Compton= 0

question1= {#adding dictionaries to build lists
        "question" : "What's your jam?",
        "A. Hips Don't Lie" : "Rio",
        "B. Sweet Home Alabama" : "Montgomery",
        "C. The Next Episode" : "Compton"
        }

question2= {
        "question": "How do you take your coffee?",
        "A. Black": "Montgomery",
        "B. I don't drink coffee": "Compton",
        "C. Local and organic" : "Rio"
        }

question3= {
        "question": "What could you eat forever?",
        "A. Beans and Rice": "Rio",
        "B. Steak and Potatoes": "Montgomery",
        "C. Tacos and Burritos": "Compton"
        }

#below turns the dictionaies into lists, allowing me to use positions as keys/values
question1_list= list(question1.keys())
question2_list= list(question2.keys())
question3_list= list(question3.keys())
print("Which city should you live in?  Find out by answering three simple questions!")

time.sleep(2)#adding time to have the prompts more user friendly

def main():
    #added the below for counters to keep track of points
    Rio= 0
    Montgomery= 0
    Compton= 0
    print("Question 1! Get ready!")
    time.sleep(.5)
    print(question1["question"])
    print(question1_list[1])
    print(question1_list[2])
    print(question1_list[3])
    while True:
        try:
            q1answer= input("Please choose either A, B, or C >")
            q1answer= q1answer.upper()#changed answer into Uppercase (potentially user put it in lower case and it didnt work)
            if q1answer not in ["A", "B" , "C"]: 
                print("please make a valid choice between A, B, or C")
                continue
            elif q1answer == "A":
                Rio += 1
            elif q1answer == "B":
                Montgomery += 1
            elif q1answer == "C":
                Compton += 1
            
            print(f"You chose {q1answer}, good choice!")
            
            break
        except: 
            print("Oopsie")
            
                

    print("Next question in 2 seconds!")
    time.sleep(2)
    print("Question 2! Get ready!")
    time.sleep(.5)
    print(question2["question"])
    print(question2_list[1])
    print(question2_list[2])
    print(question2_list[3])
    while True:
        try: 
            q2answer= input("Please choose either A, B, or C >")
            q2answer= q2answer.upper()
            if q2answer not in ["A", "B" , "C"]: 
                print("please make a valid choice between A, B, or C")
                continue
            elif q2answer == "A":
                Montgomery += 1
            elif q2answer == "B":
                Compton += 1
            elif q2answer == "C":
                Rio += 1 
            print(f"You chose {q2answer}, good choice!")
            break
        except: 
            print("Oopsie")


    print("Next question in 2 seconds!")
    time.sleep(2)
    print("Last question! Here we go!")
    time.sleep(.5)
    print(question3["question"])
    print(question3_list[1])
    print(question3_list[2])
    print(question3_list[3])
    while True:
        try:
            q3answer= input("Please choose either A, B, or C >")
            q3answer= q3answer.upper()
            if q3answer not in ["A", "B" , "C"]: 
                print("please make a valid choice between A, B, or C")
                continue
            elif q3answer == "A":
                Rio += 1
            elif q3answer == "B":
                Montgomery += 1
            elif q3answer == "C":
                Compton += 1    
            print(f"You chose {q3answer}, good choice!")
            break
        except:
            print("oopsie")
    
    print("Calculating results!  Please wait!")
    time.sleep(2)
    print("Just a moment longer!")
    time.sleep(1)

    if Rio == Montgomery or Rio == Compton or Compton == Montgomery or Compton == Rio or Montgomery == Compton or Montgomery == Rio:
        print("You have a tie! You should travel! ")
    
    elif Rio > Montgomery and Rio > Compton:
        print("You should live in Rio!")
    
    elif Montgomery > Rio and Montgomery > Compton:
        print("You should live in Montgomery!")
    
    elif Compton > Montgomery and Compton > Rio:
        print("You should live in Compton!")
    
        
main()
