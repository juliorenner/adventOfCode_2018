import os
currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split('\n')

    count2 = 0
    count3 = 0

    for line in input:
        letters = {}
        lineCount2 = 0
        lineCount3 = 0
        for letter in line:
            if (letters.has_key(letter)):
                letters[letter] += 1
                if (letters[letter] == 2):
                    lineCount2 += 1
                elif (letters[letter] == 3):
                    lineCount2 -= 1
                    lineCount3 += 1
                elif (letters[letter] == 4):
                    lineCount3 -= 1
            else:
                letters[letter] = 1
        
        if (lineCount2 > 0):
            count2 += 1
        if (lineCount3 > 0):
            count3 += 1
    
    print("Checksum: " + str(count2 * count3))
