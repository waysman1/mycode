#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('http://api.open-notify.org/iss-pass.json?lat=35.8&lon=-78.8')

    ## isstime  is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
## print the value assocaited with text"
    print(r.json())  # the .get() method returns NONE if key not found
main()

