#!/usr/bin/env python3
"""VArmstrong
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display list1[1] which will only display the second (0,1,2,3 etc) list entry
    print(list1[1])

    list2= ["juniper"]

    #extend list1 bu list2 (this will combine both lists together into one list)
    list1.extend(list2)
    print(list1)

    list3 = ["10.1.0.1", "10.2.0.1" ,  "10.3.0.1"] 
    #use the append operation to append list1 by list 3
    list1.append(list3)
    print(list1)

    print(list1[4])

    print(list1[4][0])


    

main()

