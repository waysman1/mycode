#!/usr/bin/env python3
from subprocess import call

call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ene3: ")
call(["ip", "route", "show", "dev", interface])

