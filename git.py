#!/usr/bin/env python3

import os
import time


add = str("git add *")
commit= str('git commit -m "latest update"')
push = str("git push origin HEAD")

def main(): 
    os.system("cd ~/mycode")

    os.system(f"{add}")
    time.sleep(1)
    os.system(f"{commit}")
    time.sleep(1)
    os.system(f"{push}")
    
main()
print("Success!")
