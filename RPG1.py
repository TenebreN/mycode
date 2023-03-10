#!/usr/bin/python4
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
    if rooms[currentRoom] == rooms['Castle of Knowledge']:
        if 'paper' and "programming manual" in inventory :
            win()
    print("---------------------------")

def winquit():
    print ("Thank you for playing!  You have escaped ignorance!  Keep practicing!")
    exit()
def quitgame():
    print("thank you for playing! (quitter!)")
    exit()

def win():
    print('''
    
    You have reached the castle.  
    
    a loud voice calls from above:
    
    "I am CHAD, your python instructor...  you lost the drinking game and now you are stuck here.  You have all of the tools you need. To get out, you must provide the key!
    
    Otherwise, you will rot here in ignorance.  You have three chances."

    You have learned some valuable lessons during your time in this alternate reality.  Can you provide the key to python success??
    
    ''')
    answer= input('What is the key to success?  Shout it out!\n>>')
    while answer == 'practice':
        print('no, you must SHOUT IT!')
        continue
    if answer != "PRACTICE":
        print('You have answered incorrectly.  You have XXX tries')
        counter += 1
        continue
    if answer == 'PRACTICE':
        print('''

        Chad's booming voice calls out:

        "YES!  YOU HAVE ANSWERED CORRECTLY AND ESCAPED A LIFE OF IGNORANCE!  GO FORTH, AND PRACTICE!"

        With that, you awaken in your own surroundings, an open python book in front of you.  Better get started!

        You WIN!

        ''')
        winquit()


    

# an inventory, which is initially empty
inventory = []
commands = ['go' , 'get', 'look' , 'quit', 'exit'] 
commands2= [inventory, 'north', 'south','east','west', 'up', 'down' , 'in' , 'out']
none = None
counter = 1
# a dictionary linking a room to other rooms
rooms =  {

            'dark woods' : {
			    'south' : 'small clearing' ,
			    'north' : 'foothills',
                'description' : 'You are standing in a dark, wooded forest. The air is cold, and though it is still, it seems to seep into your light clothing, and you shiver.  To the south you see a small clearing of trees, and to the north you see the ground start to rise.  East and west are blocked by trees.', 
			    'item' : 'map',
                },
            'Castle of Knowledge' : {
                'south' : 'foothills' , 
                'port2' : 'master bedroom',
                'description' : 'You are standing before a beautiful castle.  Somehow you know that this is your out of here..',
            },

            'foothills' : {
                'south' : 'dark woods',
                'north' : 'Castle of Knowledge',
                'description' : 'you are in the foothills.  Your breathing becomes labored (and your hangover doesn\'t help) as you climb. To the [south] lies the dark woods, and to the [north] you see a majestic castle ',
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
                'port1' : 'Castle of Knowledge',
                'description' : 'you have entered the master bedroom.  The smell of decay immediately hits your nostrils.  As your eyes adjust to the dark, you are shocked to see a lifeless body on the center of the bed.  You see a nametag and title pinned to the corpse\'s body.  It reads "Smith - TLG Learning Student".  In the corpse\'s hand is a piece of [paper]' , 

                'item' : 'paper',
            },
        }

items = {
            
            'map' : {
                'description' : 
                '''
                                            [ castle    ]
                                                  |
                [master]                    [ foothills ] 
                    |                             |
                [hall  ]                    [ dark woods]
                    |                             |
                [house ]  -  [courtyard] -  [small clear]
                '''

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
    if move == 'quit' or move == 'exit':
        quitgame()
    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    if ' ' not in move:
        print('Please enter a two part command')
        continue
    move = move.lower().split(" ", 1)
    
    #if they type 'go' first
    #if [currentRoom] == 'Castle of Knowledge' :
       # key= input('You have made it to the Castle of Knowledge.  Here is your opportunity to escape the land of coding ignorance and return to reality\n what is key? \n')
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
            print(move[1] + ' taken!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    if move[0] == 'look':
        if move[1] in inventory:
            print(items[move[1]]['description'])

        elif move[1] not in inventory:
            print(f'You dont have a {move[1]}')
        #elif move[1] == "paper":
            #print(items[move[1]]['description'])
        #elif move[1] == "sword":
            #print(items['sword']['description'])
        #elif move[1] == 'programming manual':
            #print(items['programming manual']['description'])
        time.sleep(5)
    if currentRoom == rooms['Castle of Knowledge']:
        win()
    
    elif move[0] not in commands:
        #try:
        print('sorry, your command was misunderstood.  Please use either \'get (item)\', \'go (direction)\', or \'look (item)\' ')
        #except: 
    #elif move[1] not in commands2:       #print('sorry')
        print('sorry, your command was misunderstood.  Please use either \'get (item)\', \'go (direction)\', or \'look (item)\' ')   
    elif move[1] =='':
        print('commands must be two-part')       #continue
win()

        
           
            
            
            #delete the item key:value pair from the room's dictionary
            
        # if there's no item in the room or the item doesn't match
    
            #tell them they can't get it
        
