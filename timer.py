import os
import time
import keyboard

pressed = False
# delay = 2 
# delayTime = 0
fortnite = 0

os.system('cls' if os.name == 'nt' else 'clear')

def timer():
    global pressed 
    # global delay
    # global delayTime
    global fortnite

    # currentTime = time.time()

    if keyboard.read_key() == "space" and pressed == False:
        startTime = time.time()
        pressed = True

    if keyboard.read_key() == "space" and pressed == True: 
        endTime = time.time()
        pressed = False
        if fortnite % 2 == 0: 
            print(round(endTime - startTime, 2))
        fortnite += 1


while True:
    timer()
