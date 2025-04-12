import numpy
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
        totalTime = round(endTime - startTime, 2)

        # every second output is being printed => otherwise would print the time between every space press
        if printCount == True: 
            print("Time: ", totalTime, "s")
            printCount = False 

            # Writing multiple lines to an existing file using writelines()
            timeString = numpy.format_float_positional(totalTime)
            sString = "s"

            with open("times.txt", "w") as f:
                f.write(timeString)
                f.write("\n")
        else:
            printCount = True 



# main loop
while True:
    timer()


