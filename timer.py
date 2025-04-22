import os
import time
import keyboard

pressed = False
printCount = True 
timesCount = 0

# clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# create times.txt file if not already there
if os.path.isfile("times.txt") == False:
    file = open("times.txt", "w")

# starts the ao5
with open("times.txt", "a") as f:
    f.write("ao5:" + "\n")

print("Press space to start and then again to stop!")

# main timer function
def timer():
    global pressed 
    global printCount
    global timesCount

    # start the timer
    if keyboard.read_key() == "space" and pressed == False:
        startTime = time.time()
        pressed = True

    # stop the timer
    if keyboard.read_key() == "space" and pressed == True: 
        endTime = time.time()
        pressed = False
        totalTime = round(endTime - startTime, 2)

        # every second output is being printed => otherwise would print the time between every space press
        if printCount == True: 
            print("Time: ", totalTime, "s")
            printCount = False 
            timesCount += 1

            # Writing multiple lines to an existing file using writelines()
            timeString = str(totalTime)
            sString = "s"
            with open("times.txt", "a") as f:
                f.write(timeString + ";" + "\n")

        elif timesCount == 5:
            with open("times.txt", "a") as f:
                f.write("\n" + "ao5:" + "\n")
            timesCount = 0
        else:
            printCount = True 



# main loop
while True:
    timer()


