import os
import re
currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split(" ")

    totalSum = 0

    def getMetadataCount(substring):
        if len(substring) == 0:
            return 0

        header = int(substring.pop(0))
        metadata = int(substring.pop(0))
        
        metadataSum = 0
        for v in range(0,header):
            metadataSum += getMetadataCount(substring)
    
        for v in range(0, metadata):
            metadataSum += int(substring.pop(0))

        return metadataSum

    print(getMetadataCount(input))
