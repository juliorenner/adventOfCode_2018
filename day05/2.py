import os
import operator

currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    def removeCharacter(letter):
        line = input.replace(letter.lower(), '')
        return line.replace(letter.upper(), '')

    def countConflicts(currentString):
        resultString = ""
        for letter in currentString:
            if (resultString == ""):
                resultString += letter
            else: 
                lastLetter = resultString[len(resultString)-1]
                
                if letter != lastLetter and (letter.lower() == lastLetter.lower()):
                    resultString = resultString[:-1]
                else:
                    resultString += letter
        
        return resultString

    input = inputFile.read()

    conflictsMap = {}

    resultString = ""
    for letter in input:
        if not letter.upper() in conflictsMap:
            currentString = removeCharacter(letter)
            conflictsMap[letter.upper()] = countConflicts(currentString)
    
    highest = None
    for v in conflictsMap:
        if highest == None:
            highest = v
        elif len(conflictsMap[v]) < len(conflictsMap[highest]):
            highest = v

    print("answer: " + str(len(conflictsMap[highest])))
