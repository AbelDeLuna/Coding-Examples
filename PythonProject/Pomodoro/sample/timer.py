from time import time, sleep
import asyncio

class timerLogic:
    def __init__(self, studyTime, breakTime):
        self.studyTime = studyTime
        self.breakTime = breakTime
        self.timeRemaining = 0
        self.timeDisplay = ""
    def setTimer(self):
        self.timeRemaining = time() + (self.studyTime * 60)
    def isTimeRemaining(self):
        if ( self.timeRemaining > 0):
            return 
        else:
            return False
    async def startTimer(self, timeAmmount):
        print("running")
        while(self.timeRemaining > 1):
            self.timeRemaining = timeAmmount - time()
            minutes = int(self.timeRemaining // 60)
            seconds = int(self.timeRemaining % 60)
            self.timeDisplay = '{0:02d}:{1:02d}'.format(minutes, seconds)
            print(self.timeDisplay)
            await asyncio.sleep(1)
