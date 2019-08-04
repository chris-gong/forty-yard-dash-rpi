from multiprocessing import Process
import time
import threading
import queue
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from stopWatch import App

global startingChannel, finishingChannel, raceStarted, raceInProgress, raceFinished, stopWatch, startingThread, finishingThread
raceStarted = False
raceInProgress = False
raceFinished = False
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
startingChannel = AnalogIn(ads, ADS.P1)
finishingChannel = AnalogIn(ads, ADS.P0)

def startingLine():
    global startingChannel, finishingChannel, raceStarted, raceInProgress, raceFinished, stopWatch, startingThread
    print("starting line function called")
    while(True):
        #print("starting line " + str(raceInProgress) + " " + str(startingChannel.value))
        if(not raceInProgress and int(startingChannel.value) > 1000):
            print("starting line laser beam broken" + str(startingChannel.value))
            #stopWatch.reset()
            finishingThread = threading.Thread(target=finishLine)
            finishingThread.start()
            stopWatch.start()
            raceInProgress= True
            
            print("done")
            #break
            

    
def finishLine():
    global startingChannel, finishingChannel, raceStarted, raceInProgress, raceFinished, stopWatch, startingThread, finishingThread
    print("finish line function called")
    while(True):
        #print("finish " + str(finishingChannel.value))
        
        if(int(finishingChannel.value) > 1800):
            print("finish line laser beam broken " + str(int(finishingChannel.value)))
            stopWatch.stop()
            raceInProgress = False
            break
        
    
def main():
    global startingChannel, finishingChannel, raceStarted, raceInProgress, raceFinished, stopWatch, startingThread, finishingThread
    stopWatch = App()
    stopWatch.stop()
    print("main function called")
    
    
    startingThread = threading.Thread(target=startingLine)
            
    
    startingThread.start()
    
    
    
    stopWatch.root.mainloop()

    
if __name__ == "__main__":
    main()
    
    
        
    
