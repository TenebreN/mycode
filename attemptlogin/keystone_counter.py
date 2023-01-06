#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
GETorPOST = 0
failips = []
# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
# turn the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()
# loop over the list of lines
for line in keystone_file_lines:
    # if this 'fail pattern' appears in the line...
    if "Authorization failed" in line:
        #print(line)
        print(line.split()[-1])
        ip= line.split()[-1]
        failips.append(ip)
    if "GET" or "POST" in line:
        GETorPOST += 1
        #print(line)
        loginfail += 1 # this is the same as loginfail = loginfail + 1
        with open("errorfile.txt" , "a") as errorfile:
            errorfile.write(line + "\n")
        
print(f"The number of failed log in attempts is {loginfail}")


    
print(f"The number of GET or POST requests is {GETorPOST}")
print(f"the unauthorized IPs are {failips}")
keystone_file.close() # close the open file

