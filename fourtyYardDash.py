import RPi.GPIO as GPIO
import time
import threading
import queue
from gpiozero import LightSensor
from stopWatch import App

global startingLinePin, finishLinePin, startingLdr, finishLdr, raceStarted, raceInProgress, raceFinished, stopWatch
startingLinePin = 4 #pin away from the Pi
finishLinePin = 17
startingLdr = LightSensor(pin = startingLinePin, charge_time_limit = 0.1)
finishLdr = LightSensor(pin = finishLinePin, charge_time_limit = 0.1)
raceStarted = False
raceInProgress = False
raceFinished = False
GPIO.setmode(GPIO.BCM)

def startingLine():
    global startingLinePin, finishLinePin, startingLdr, finishLdr, raceStarted, raceInProgress, raceFinished, stopWatch
    print("starting line function called")
    while(True):
        print(startingLdr.value)
        if(startingLdr.value < 0.85):
            print("starting line laser beam broken")
            stopWatch.reset()
            stopWatch.start()
            break
    '''
    while(True):
        count = 0
        GPIO.setup(startingLinePin, GPIO.OUT)
        GPIO.output(startingLinePin, GPIO.LOW)
        time.sleep(0.0001)

        GPIO.setup(startingLinePin, GPIO.IN)
        
        while(GPIO.input(startingLinePin) == GPIO.LOW and count < 1000):
            count += 1

        if(count >= 1000):
            print("starting line laser beam broken")
            stopWatch.reset()
            stopWatch.start()
            break
    '''
    
def finishLine():
    global startingLinePin, finishLinePin, startingLdr, finishLdr, raceStarted, raceInProgress, raceFinished, stopWatch
    print("finish line function called")
    while(True):
        print(finishLdr.value)
        if(finishLdr.value < 0.75):
            print("finish line laser beam broken")
            stopWatch.stop()
            break
    
def main():
    global startingLinePin, finishLinePin, startingLdr, finishLdr, raceStarted, raceInProgress, raceFinished, stopWatch
    stopWatch = App()
    stopWatch.stop()
    print("main function called")
    
    startThread = threading.Thread(target=startingLine)
    finishThread = threading.Thread(target=finishLine)
    
    startThread.start()
    finishThread.start()
    
    stopWatch.root.mainloop()

    
if __name__ == "__main__":
    main()
    
    
        
    
