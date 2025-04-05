import time
import keyboard

time.sleep(1)
while True:
    try:
        if keyboard.is_pressed("g"):
            startTime = time.time()
            time.sleep(1)
            endTime = time.time() 
            print(endTime - startTime)
            break
    except:
        print("fortnite")
        break

