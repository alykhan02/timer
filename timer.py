"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 
import random

# displays Players stand
print("Players Stand!!")

# sleeps for random time between 5-25 sec 
time.sleep(random.randint(5, 25))

# sleep is over program displays time up
print("Times Up!!! Last to sit down wins!")




