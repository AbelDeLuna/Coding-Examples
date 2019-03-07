import subprocess as sp

sp.run('TASKKILL /F /FI "IMAGENAME eq Skype*"')
#TODO implement a sleep cycle. Need to determine how long Skype waits before relaunching itself
