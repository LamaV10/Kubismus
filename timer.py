import os
import time
import keyboard

pressed = False
printCount = True 
# clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')

print("Press space to start and then again to stop!")
# main timer function
def timer():
    global pressed 
    global printCount

    # start the timer
    if keyboard.read_key() == "space" and pressed == False:
        startTime = time.time()
        pressed = True

    # stop the timer
    if keyboard.read_key() == "space" and pressed == True: 
        endTime = time.time()
        pressed = False
        # every second output is being printed => otherwise would print the time between every space press
        if printCount == True: 
            print(round(endTime - startTime, 2))
            printCount = False 
        else:
            printCount = True 


while True:
    timer()
