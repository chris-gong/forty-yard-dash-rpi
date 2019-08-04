import time
from tkinter import *

global start_time, running
start_time = 0
running = False

class App():
    def reset(self):
        global start_time, running
        running = False
        self.t.set("00:00")
        
    def start(self):
        global start_time, running
        print("timer started")
        start_time = time.time() * 100
        running = True
        self.start_timer()
        
    def start_timer(self):
        global start_time, running
        self.timer()
        
    def stop(self):
        global start_time, running
        running = False
        
    def timer(self):
        global start_time
        print("timer timer called")
        while(True):
            #print("running " + str(running))
            if(running):
                #print("wut")
                current_time = time.time() * 100
                difference = current_time - start_time
                s = int(difference / 100)
                cs = int(difference % 100)
                self.d = str(s) + ":" + str(cs)
                
                self.t.set(self.d)
                
    def __init__(self):
        self.root = Tk()
        self.root.title("Stop Watch")
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)
        self.t = StringVar()
        self.t.set("00:00")
        self.lb = Label(self.root, textvariable = self.t)
        self.lb.config(font=("Courier 425 bold"))
        self.lb.pack(side="top")
        
        