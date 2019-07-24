#!/usr/bin/env python3

#this library allows us to generate uuid value.
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generation UUIDs...")

# range is requred because an int connot be looped.
for rando in range(howmany):
    print( uuid.uuid4() )

