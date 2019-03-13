import time

class timer:
    def __init__(self, studyTime, breakTime):
        self.studyTime = studyTime
        self.breakTime = breakTime
        self.timeRemaining = 0
    def startTime(self):
        endTime = time.time() + (self.studyTime * 60)
        self.countDown(endTime)
    def countDown(self, timeAmmount):
        self.timeRemaining = timeAmmount - time.time()
        minutes = int(self.timeRemaining // 60)
        seconds = int(self.timeRemaining % 60)
        time.sleep(1)
        print("time remaining - ", minutes, ":", seconds)
        if self.timeRemaining > 1:
            self.countDown()
        else:
            return("done")






if __name__ == "__main__":
    test = timer(1, 10)
    test.startTime()

    