import os
import re
currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split("\n")

    rootMap = {}
    lockerCount = {}
    timeMap = {}

    for v in input:
        groups = re.match(r"Step ([aA-zZ]) .* step ([aA-zZ]) .*", v)

        father = groups[1]
        children = groups[2]

        if not father in timeMap:
            timeMap[father] = 0
        if not children in timeMap:
            timeMap[children] = 0

        if father in rootMap:
            rootMap[father].append(children)
            rootMap[father].sort()
        else:
            rootMap[father] = [children]

        if children in lockerCount:
            lockerCount[children] += 1
        else:
            lockerCount[children] = 1

    rootKeys = rootMap.keys()
    rootKey = rootKeys - lockerCount.keys()
    
    result = ""
    unlocked = []
    
    timeArray = list(timeMap.keys())
    timeArray.sort()

    for i in rootKey:
        unlocked.append((i, timeArray.index(i)+60))

    unlocked.sort()
    seconds = 0

    workers = {}
    workersNumber = 5
    while len(lockerCount) > 0 or len(unlocked) > 0 or len(workers) > 0:
        
        while (len(unlocked) > 0 and len(workers) < workersNumber):
            letter = unlocked.pop(0)
            workers[letter[0]] = letter[1]

        deletion = []
        for w in workers:
            workers[w] += -1
            
            if workers[w] < 0:
                deletion.append(w)
                if (w in rootMap):
                    childrens = rootMap[w]
                    for children in childrens:
                        lockerCount[children] += -1

                        if lockerCount[children] == 0:
                            del lockerCount[children]
                            unlocked.append((children, timeArray.index(children)+60))

                    unlocked.sort()
        seconds += 1
        for d in deletion:
            del workers[d]
        
    print(seconds)
