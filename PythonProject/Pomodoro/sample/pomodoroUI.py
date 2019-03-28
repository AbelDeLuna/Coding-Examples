from tkinter import *
from timer import timerLogic

class display:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pomodoro")
        self.TimeRemainingDisplay = StringVar()
        self.buttonTitle = StringVar()
        self.count = timerLogic()
        self.create_widget()
        self.root.mainloop()
    def create_widget(self):
        #time display
        self.TimeRemainingDisplay.set("00:00")
        Label (self.root, textvariable=self.TimeRemainingDisplay).grid(row=1, column=1)
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
        self.buttonTitle.set("Study")
    def countDown(self):
        self.count.setTimer(self.studyTime, self.breakTime)
        #TODO
    def pauseTimer(self):
        self.count.isPaused = not self.count.isPaused
        self.buttonToggle()
    def buttonToggle(self):
        if(self.buttonTitle.get() == "Pause"):
            #Pause State -> Current State (Study | Break)
            self.buttonTitle.set(self.count.timeState)
        elif(self.buttonTitle.get() == "Study"):
            if (self.count.timeRemaining == 0):
                self.buttonTitle.set("Break")
                self.count.timeState = "Break"
            else:
                self.buttonTitle.set("Pause")
        elif(self.buttonTitle.get() == "Break"):
            if(self.count.timeRemaining == 0):
                self.buttonTitle.set("Study")
                self.count.timeState = "Study"
            else:
                self.buttonTitle.set("Pause")
        else:
            print("Error")
    def updateTimeDisplay():
        self.timeDisplay = '{0:02d}:{1:02d}'.format(self.count.minRemaining, self.count.secRemaining)

        
        

        


