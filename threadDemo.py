import threading, time
print("start of program!")

def takeANape():
    time.sleep(5)
    print("Wake Up!")

threadObj = threading.Thread(target = takeANape)
threadObj.start()

print("End of program")
