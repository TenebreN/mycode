#!/usr/bin/env python3

beer=0
beer=int(input("How many beers would you like to start with?"))

try: 
    for beer2 in range(beer , -1,-1):
        beer2 -= 1
        print(f"{beer} bottles of beer on the wall, {beer} bottles of beer, take one down, pass it around, {beer2} bottles of beer on the wall!")
        beer -= 1
    if beer2 == 0: 
        print("no more bottles of beer on the wall, no more bottles of beer!  The song is over, thank god almighty, no more bottles of beer on the wall")
except: 
    print("i dont know")
