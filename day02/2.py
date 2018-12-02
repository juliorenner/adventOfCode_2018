import os
currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split('\n')

    def getStringsDifference(lines):
        for i, line in enumerate(lines):
            for j in range(i+1, len(lines)-1):
                nextLine = lines[j]
                differs = 0
                isSimilar = True
                index = None
                for k, letter in enumerate(line):
                    if (letter != nextLine[k]):
                        if (differs > 0):
                            isSimilar = False
                            break
                        else:
                            differs += 1
                            index = k

                if isSimilar:
                    return [line, index]
                    
    difference = getStringsDifference(input)

    # not threating scenarios like difference in the last character.
    result = difference[0][:difference[1]] + difference[0][difference[1]+1:]
    print("The answer is: " + ())
