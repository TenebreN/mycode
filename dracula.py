#!/usr/bin/env python3
"""This is the Dracula script | VArmstrong"""
vampirec = 0
with open("dracula.txt" , "r") as foo:
    with open("vampytimes.txt" , "a") as fang: 
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                vampirec += 1
                fang.write(line)
print(vampirec)
        