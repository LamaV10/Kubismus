import os
import time
import keyboard

pressed = False
printCount = True 

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
        if printCount == True: 
            print(round(endTime - startTime, 2))
            printCount = False 
        else:
            printCount = True 


while True:
    timer()
