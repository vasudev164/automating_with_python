# stopWatch.py --> A simple stopwatch program using python time module
# The functions we use in this file are ---> time.time(), time.sleep(tsec)

import time

# Display the programs instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()
print("started.")
startTime = time.time()
lastTime = startTime
lapNum = 1

# TODO : Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"Lap : {lapNum} , timetaken in lap - {lapTime} , total time finished - {totalTime} ")
        lastTime = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print("\n Done.")
