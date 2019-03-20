from time import time, sleep

class timer:
    def __init__(self, studyTime, breakTime):
        self.studyTime = studyTime
        self.breakTime = breakTime
        self.timeRemaining = 0
        self.timeDisplay = ""
    def startTime(self):
        self.timeRemaining = time() + (self.studyTime * 60)
        self.countDown(self.timeRemaining)
    def countDown(self, timeAmmount):
        while self.timeRemaining > 1:
            self.timeRemaining = timeAmmount - time()
            minutes = int(self.timeRemaining // 60)
            seconds = int(self.timeRemaining % 60)
            self.timeDisplay =  '{0:02d}:{1:02d}'.format(minutes, seconds)
            sleep(1)
            print(self.timeDisplay)