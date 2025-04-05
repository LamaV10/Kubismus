import time
import keyboard

pressed = False

while True:
    if keyboard.read_key() == "space" and pressed == False:
        startTime = time.time()
        pressed = True

    if keyboard.read_key() == "space" and pressed == True:
        endTime = time.time()
        pressed = False
        break

print(round(endTime - startTime, 2))

