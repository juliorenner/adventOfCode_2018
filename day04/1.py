import os
import re
import collections
import numpy as np

currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split('\n')

    calendar = {}

    for i in input:
        regex = re.match(r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (.+)", i)

        year = regex.group(1)
        month = regex.group(2)
        day = regex.group(3)
        hour = regex.group(4)
        minute = regex.group(5)

        key = year + month + day + hour + minute
        calendar[int(key)] = i

    minuteMap = {}
    currentGuard = None
    asleepMinute = 0
    for i in sorted(calendar.items()):
        regex = re.match(r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (.+)", i[1])

        hour = regex.group(4)
        minute = regex.group(5)

        action = regex.group(6)

        guardChange = re.match(r".*#([0-9]+)", action)
        if (guardChange):
            currentGuard = guardChange.group(1)
            if (not currentGuard in minuteMap):
                minuteMap[currentGuard] = np.zeros(60)
            
        
        elif (action == "falls asleep" and currentGuard != None):
            asleepMinute = int(minute)
        
        elif (action == "wakes up"):
            for r in range(asleepMinute, int(minute)):
                if (currentGuard != None):
                    minuteMap[currentGuard][r] = minuteMap[currentGuard][r] + 1
    
    guardWithMoreMinutes = 0
    guardMinutes = 0
    for i in minuteMap:
        if (guardWithMoreMinutes == 0):
            guardMinutes = np.sum(minuteMap[i])
            guardWithMoreMinutes = i
        gMinutes = np.sum(minuteMap[i])
        if (guardMinutes < gMinutes):
            guardMinutes = gMinutes
            guardWithMoreMinutes = i
        
    print(int(guardWithMoreMinutes) * minuteMap[guardWithMoreMinutes].argmax())


