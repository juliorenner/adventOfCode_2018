import os
import numpy as np

currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split('\n')

    MAX_DIST = 10000
    xCoordinates = np.zeros(len(input))
    yCoordinates = np.zeros(len(input))
    
    for i, value in enumerate(input):
        currentCoordinates = value.split(', ')
        xCoordinates[i] = int(currentCoordinates[1])
        yCoordinates[i] = int(currentCoordinates[0])
    
    xMax = xCoordinates.max()
    yMax = yCoordinates.max()

    matrix = np.zeros((xMax + 1, yMax + 1))

    def calculateDistance(x, y, currentCoord):
        dX = abs(currentCoord[0] - x)
        dY = abs(currentCoord[1] - y)
        return  dX + dY

    def isSafe(mapCoordinates, x, y):
        distance = 0
        for v in mapCoordinates:
            currentDistance = calculateDistance(x, y, mapCoordinates[v])
            if (distance + currentDistance) >= MAX_DIST:
                return False
            distance += currentDistance

        return True
        

    mapCoordinates = {}
    for i, x in enumerate(xCoordinates):
        mapCoordinates[i+1] = (x, yCoordinates[i])

    x = 0
    shape = np.shape(matrix)

    # May the coordinate should not be considered as unsafe
    while (x < shape[0]):
        y = 0
        while (y < shape[1]):
            if matrix[x,y] == 0:
                matrix[x,y] = isSafe(mapCoordinates,x,y)
        
            y += 1
        x += 1

    print(np.count_nonzero(matrix))


    

