import os
import time
import keyboard

pressed = False
finished = False
delay = 1 
delayTime = 0

os.system('cls' if os.name == 'nt' else 'clear')

def timer():
    global pressed 
    global finished
    global delay
    global delayTime

    currentTime = time.time()

    if delay + delayTime <= currentTime: 
        if keyboard.read_key() == "space" and pressed == False:
            startTime = time.time()
            pressed = True
            delayTime = time.time()

    if keyboard.read_key() == "space" and pressed == True: 
        endTime = time.time()
        print(round(endTime - startTime, 2))
        pressed = False
        finished = True


while True:
    timer()
