#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'WoW Raid Readiness Check '

# wrap connection in a float() to accept decimals as num
level= float(input("Type in Current Item Level :  "))

# if input value was higher or equal to 520
if level >= 520:
    message = message + 'Get Some.'
elif level >= 400:
    message = message + 'Put in more work.'
elif level >= 200:
    message = message + 'Get a new Guild.'
else:
    message = message + 'Sweetie you might want to change games.'
print(message)
