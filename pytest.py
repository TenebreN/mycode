def lose():
    print('loser')
    exit()

def test():
    left = 2
    counter = 0
    answer = ' '    
    while counter < 3 and (answer != 'PRACTICE' and answer != 'practice' ):
        answer= input('What is the key to success?  Shout it out!\n>>')
        counter +=1
     
    
    
       
     
        if answer == 'PRACTICE':
            print('''

            Chad's booming voice calls out:

            "YES!  YOU HAVE ANSWERED CORRECTLY AND ESCAPED A LIFE OF IGNORANCE!  GO FORTH, AND PRACTICE!"

            With that, you awaken in your own surroundings, an open python book in front of you.  Better get started!

            You WIN!

     
                ''')
    
        
    
        elif counter == 3:
            print('Chad shouts "YOU DID NOT LEARN YOUR LESSON, AND MUST STAY HERE FOREVER!"') 
            lose()

        elif answer == 'practice':
            print('no, you must SHOUT IT!')
            test()
        else:
            print(f"Try again, you have {left} more tries ")
            left -=1

test()