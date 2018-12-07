import os
import re
currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split("\n")

    rootMap = {}
    lockerCount = {}

    for v in input:
        groups = re.match(r"Step ([aA-zZ]) .* step ([aA-zZ]) .*", v)

        father = groups[1]
        children = groups[2]

        if father in rootMap:
            rootMap[father].append(children)
            rootMap[father].sort()
        else:
            rootMap[father] = [children]

        if children in lockerCount:
            lockerCount[children] += 1
        else:
            lockerCount[children] = 1

    rootKey = rootMap.keys() - lockerCount.keys()
    result = ""
    unlocked = []
    for i in rootKey:
        unlocked.append(i)

    unlocked.sort()

    while len(unlocked) > 0:
        key = unlocked.pop(0)
        result = result + key

        if key in rootMap:
            childrens = rootMap[key]

            for children in childrens:
                lockerCount[children] += -1

                if lockerCount[children] == 0:
                    del lockerCount[children]
                    unlocked.append(children)
            
            unlocked.sort()
        
    print(result)
