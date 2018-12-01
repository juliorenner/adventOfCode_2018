import os
currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split('\n')

    frequencyHash = {}
    frequencySum = 0

    i = 0
    while True:
        frequencySum += int(input[i])

        if not frequencyHash.has_key(frequencySum):
            frequencyHash[frequencySum] = 1
        else:
            print(frequencySum)
            break
        
        i = (i+1) % len(input)