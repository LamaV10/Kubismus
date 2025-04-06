import os
import time
import keyboard

pressed = False
printCount = 0

os.system('cls' if os.name == 'nt' else 'clear')

print("Press space to start and then again to stop!")

def timer():
    global pressed 
    global printCount

    if keyboard.read_key() == "space" and pressed == False:
        startTime = time.time()
        pressed = True

    if keyboard.read_key() == "space" and pressed == True: 
        endTime = time.time()
        pressed = False
        if printCount % 2 == 0: 
            print(round(endTime - startTime, 2))
        printCount += 1


while True:
    timer()
