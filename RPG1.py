#!/usr/bin/python3
"""Role Playing | VArmstrong"""

import time

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      look [item]
      quit
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print(rooms[currentRoom]['description'])
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

def quitgame():
    print("thank you for playing! (quitter!)")
    exit()

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms =  {

            'dark woods' : {
			    'south' : 'small clearing' ,
			    'description' : 'You are standing in a dark, wooded forest. The air is cold, and though it is still, it seems to seep into your light clothing, and you shiver.  To the south you see a small clearing of trees, and to the north you see the ground start to rise.  East and west are blocked by trees.', 
			    'item' : 'map',
                },

            'small clearing' : {
                  'north' : 'dark woods' ,
                  'west' : 'house courtyard' ,
                  'description' : 'You are standing in a small clearing of trees.  The open air allows you to catch your breath.  You see woods to the north, and a small house to the west. The other ways are blocked.' , 

                },
            'house courtyard' : {
                'east' : 'small clearing',
                'west' : 'house' ,
                'description' : 'You are in the courtyard of a decrepit house.  Broken bottles, like your programming hopes and dreams, lay strewn about and discarded.  Further west is the shack entrance. The small clearing is behind you, and the other ways are blocked.',
                
                },
            'house' : {
                'up' : 'second floor',
                'east' : 'house courtyard',
                'description' : 'You are inside the decrepit house. It smells musty and rotten.  Discarded many old books sit on a broken table.  Going (up) you see a staircase.' ,
                'item' : 'programming manual' ,
           },
            'second floor' : {
                'down' : 'house',
                'in' : 'master bedroom' , 
                'description' : 'at the top of the staircase you emerge into a hall. The entire area smells like piss and bad decisions.  There is a single closed door at the end of the hall.  Go [in] or go [down]?',

                
            },
            'master bedroom' : {
                'out' : 'second floor',
                'description' : 'you have entered the master bedroom.  The smell of decay immediately hits your nostrils.  As your eyes adjust to the dark, you are shocked to see a lifeless body on the center of the bed.  You see a nametag and title pinned to the corpse\'s body.  It reads "Smith - TLG Learning Student".  In the corpse\'s hand is a piece of [paper]' , 

                'item' : 'paper'
            },
        }

items = {
            
            'map' : {
                'description' : 'this map is blank, like your mind when trying to remember commands',
                },

            'sword' : {
                'description' : 'the sword is razor sharp, like the margin you had passing previous certification tests',
                },
            
            'paper' : {
                 'description' : '''on the paper is printed: 
                 
                 I should have studied!

                 practice is the key!'''
                },
            
            'programming manual' : {
                'description' : 'the manual is dusty but unused.  Why didn\'t the previous owner practice?',
            }, 
        }
# start the player in the Hall
currentRoom = 'dark woods'
itemlist = ''
showInstructions()
playername= input("Welcome to XXXXXX!  A game in which you are the guinea pig at the mercy of my very questionable python skills! \n \nPlease enter your name: \n")

print(f"You awaken with a start, in an unfamiliar land wearing dirty leather clothing.  You have a splitting headache.  Your last memory was sitting at your computer,  playing a drinking game with your python instructors Chad and Paul.  Every time you made a mistake in your python coding, you had to take a drink.  Double if you were caught hardcoding.  Obviously, you drank too much...")

time.sleep(2)

print(f'''
    ...your only hope now is to somehow escape from this strange dimension and get out of your infinite loop.
    

    good luck, {playername}
    ''')
# breaking this while loop means the game is over

time.sleep(2)



while True:
    showStatus()
    
    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    elif move[0] == 'look':
        if move[1] in inventory:
            print(items[move[1]]['description'])
        #elif move[1] == "paper":
            #print(items[move[1]]['description'])
        #elif move[1] == "sword":
            #print(items['sword']['description'])
        #elif move[1] == 'programming manual':
            #print(items['programming manual']['description'])
        time.sleep(5)
    elif move[0] == 'quit':
        quitgame()    
    else:
            print('sorry')
        

        
           
            
            
            #delete the item key:value pair from the room's dictionary
            
        # if there's no item in the room or the item doesn't match
    
            #tell them they can't get it
        
