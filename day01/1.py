import os
currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split('\n')

    frequencySum = 0

    for f in input:
        frequencySum += int(f)

    print(frequencySum)