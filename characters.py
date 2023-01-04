marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
x= input("Character name: >")
y= input("Stat: >")

# what you have here is great- so x will be the name of the character, y will be the stat (real name, powers, or archenemy)

# this is the first part of what you're supposed to print out:
# <x>'s <y> is:
# ^ try printing out just that much for now
print(f"{x}'s {y} is:")
                    # now in that last {} we have to slice down to the final value
                    # so marvelchars["Hulk"]["powers"] would return "superstrength"
                    # so just replace "Hulk" and "powers" with x and y!

print(f"{x}'s {y} is: {marvelchars[x][y]}")

