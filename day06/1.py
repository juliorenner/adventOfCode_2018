import os
import numpy as np

currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split('\n')


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

    def getNearest(mapCoordinates, x, y):
        coordinates = None
        distance = 0
        conflict = False
        for v in mapCoordinates:
            currentDistance = calculateDistance(x, y, mapCoordinates[v])
            if coordinates == None:
                coordinates = v 
                distance = currentDistance
            else:
                if (currentDistance == distance ):
                    conflict = True

                if (currentDistance < distance):
                    coordinates = v
                    distance = currentDistance
                    conflict = False
        
        if conflict:
            return -1
        
        return coordinates
        

    mapCoordinates = {}
    for i, x in enumerate(xCoordinates):
        mapCoordinates[i+1] = (x, yCoordinates[i])

    x = 0
    shape = np.shape(matrix)

    while (x < shape[0]):
        y = 0
        while (y < shape[1]):
            if matrix[x,y] == 0:
                matrix[x,y] = getNearest(mapCoordinates,x,y)
        
            y += 1
        x += 1
    
    
    for i, value in enumerate(matrix[0]):
        if mapCoordinates.has_key(value):
            mapCoordinates.pop(value, None)
        if mapCoordinates.has_key(matrix[shape[0]-1, i]):
            mapCoordinates.pop(matrix[shape[0]-1, i], None)
        
    for i, value in enumerate(matrix):
        if mapCoordinates.has_key(value[0]):
            mapCoordinates.pop(value[0], None)
        if mapCoordinates.has_key(matrix[i, shape[1]-1]):
            mapCoordinates.pop(matrix[i, shape[1]-1], None)


    countMap = {}
    x=0
    while (x < shape[0]):
        y = 0
        while (y < shape[1]):
            if mapCoordinates.has_key(matrix[x,y]): 
                if countMap.has_key(matrix[x,y]):
                    countMap[matrix[x,y]] += 1
                else:
                    countMap[matrix[x,y]] = 1
        
            y += 1
        x += 1
            
     
    print(max(countMap, key=countMap.get))


    

