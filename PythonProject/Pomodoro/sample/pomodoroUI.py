from tkinter import *
from timer import timerLogic
import asyncio

class display:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pomodoro")
        self.create_widget()
        self.root.mainloop()
    def create_widget(self):
        #time display

        #time selections        
        minutesSelectable = [x for x in range(60) if x % 5 == 0]
        self.selectStudy = IntVar(self.root)
        self.selectStudy.set(minutesSelectable[0])
        self.selectBreak = IntVar(self.root)
        self.selectBreak.set(minutesSelectable[0])
        self.studyTime = OptionMenu(self.root, self.selectStudy, *minutesSelectable)
        self.breakTime = OptionMenu(self.root, self.selectBreak, *minutesSelectable)
        Label (self.root, text="Select study time:").grid(row=2, column=2)
        self.studyTime.grid(row=2, column=3)
        Label (self.root, text="Select break time:").grid(row=3, column=2)
        self.breakTime.grid(row=3, column=3)
        Label (self.root, text=self.selectBreak.get()).grid(row=1, column=2)
        self.startBttn = Button(self.root, text="Begin", command = lambda: self.countDown())
        self.startBttn.grid(row=4, column=3)
    def countDown(self):
        count = timerLogic(self.selectStudy.get(), self.selectBreak.get())
        Label (self.root, text=count.timeDisplay).grid(row=4,column=2)
        print(count.isTimeRemaining())
        count.setTimer()
        asyncio.run(count.startTimer(count.timeRemaining))
        print(count.isTimeRemaining())
        
        

        


