#!/usr/bin/env python3
# parse keystone.common.wswi and return number of failed login attempts
loginfail = 0
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")
keystone_file_lines=keystone_file.readlines()
for line in keystone_file_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
    else:
        print(line) 
print("The number of failed log in attempts is " + str(loginfail))

