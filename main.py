
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys

import time

import random


time.sleep(5)

while True:
    press(key='ESC', sec=0)
    timer = random.randint(1, 15)
    time.sleep(timer)
