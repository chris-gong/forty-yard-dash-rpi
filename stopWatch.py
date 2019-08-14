import time
from tkinter import *

global start_time, running
start_time = 0
running = False

class App():
    def reset(self):
        global start_time, running
        running = False
        self.time.set("00.00")
        
    def start(self):
        global start_time, running
        print("timer started")
        start_time = time.time()
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
        print("timer timer function called")
        while(True):
            if(running):
                current_time = time.time()
                difference = current_time - start_time
                
                self.time.set(“{:.2f}”. format(difference))
                
    def __init__(self):
        self.root = Tk()
        self.root.title("Stop Watch")
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)
        self.time = StringVar()
        self.time.set("00.00")
        self.lb = Label(self.root, textvariable = self.time)
        self.lb.config(font=("Courier 425 bold"))
        self.lb.pack(side="top")
        
        
