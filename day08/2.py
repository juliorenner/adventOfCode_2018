class Node:
    def __init__(self, headers, metadataAmount):
        self.headers = headers
        self.metadataAmount = metadataAmount
        self.metadataIndexes = []
        self.childrens = []
        self.weight = 0

    def addChildrens(self, childrens):
        self.childrens.append(childrens)
    
    def addMetadataIndex(self, index):
        self.metadataIndexes.append(int(index))

    def sumMetadataIndexes(self):
        metadataSum = 0
        for i in self.metadataIndexes:
            metadataSum += i
        return metadataSum
        

    def calculateWeight(self):
        if self.weight > 0:
            return self.weight

        for i in self.metadataIndexes:
            if self.headers == 0:
                self.weight = self.sumMetadataIndexes()
                return self.weight

            metadataIndex = i-1
            if metadataIndex < len(self.childrens) and metadataIndex >= 0:
                self.weight += self.childrens[metadataIndex].calculateWeight()
            
        return self.weight

import os
import re
currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split(" ")

    totalSum = 0

    def generateTree(substring):
        if len(substring) == 0:
            return 0

        header = int(substring.pop(0))
        metadata = int(substring.pop(0))
        
        node = Node(header, metadata)
        for v in range(header):
            node.addChildrens(generateTree(substring))
    
        for v in range(metadata):
            node.addMetadataIndex(substring.pop(0))

        return node

    node = generateTree(input)
    node.calculateWeight()
    print(node.weight)
