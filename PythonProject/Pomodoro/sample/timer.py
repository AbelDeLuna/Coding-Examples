from time import time, sleep

class timerLogic:
    def __init__(self):
        self.timeAmount = 0
        #TODO Implement better method of toggleing isPaused when time has run out 
        # without having to updateTimer()
        self.isPaused = True
        self.startTime = 0
        self.endTime = 0
        self.pausedTime = [0,0]
        self.minRemaining = 0
        self.secRemaining = 0
    def setTimer(self, timeAmount):
        self.startTime = time() 
        self.timeAmount = timeAmount
        self.isPaused = False
        self.endTime = self.startTime + (self.timeAmount * 60)
    def updateTimer(self):
        if(self.isPaused == False):
            timeLeft = self.endTime - time()
            if (timeLeft != 0):
                self.minRemaining = int(timeLeft // 60)
                self.secRemaining = int(timeLeft % 60)
            else:
                self.minRemaining = 0
                self.secRemaining = 0
                self.isPaused = True
        return (self.minRemaining, self.secRemaining)
    def pauseTime(self):
        if (self.isPaused == False):
            #Enter Paused State
            self.pausedTime[0] = time()
            self.isPaused = True
        else:
            #Exit Paused State
            self.pausedTime[1] = time()
            self.endTime += self.pausedTime[1] - self.pausedTime[0]
            self.isPaused = False
            self.pausedTime[0] = 0
            self.pausedTime[1] = 0



