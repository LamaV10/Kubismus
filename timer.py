import time
import keyboard

pressed = False

def timer():
    global pressed 

    if keyboard.read_key() == "space" and pressed == False:
        startTime = time.time()
        pressed = True

    if keyboard.read_key() == "space" and pressed == True:
        endTime = time.time()
        print(round(endTime - startTime, 2))
        pressed = False

while True:
    timer()
