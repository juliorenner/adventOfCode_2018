import os

currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read()

    resultString = ""
    for i, letter in enumerate(input):
        if (resultString == ""):
            resultString += letter
        else: 
            lastLetter = resultString[len(resultString)-1]
            
            if letter != lastLetter and (letter.lower() == lastLetter.lower()):
                resultString = resultString[:-1]
            else:
                resultString += letter
                
                
    print(resultString)
    print(len(resultString))
