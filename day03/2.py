import os
import re
import numpy as np

currentDir = os.path.dirname(__file__)

with open(os.path.join(currentDir, 'input.txt'), 'r') as inputFile:
    input = inputFile.read().split('\n')

    overlap = {}

    matrix = np.zeros((1050,1050))
    for i in input:
        regex = re.match(r"#([0-9]*) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", i)
        
        id = int(regex.group(1))
        overlap[id] = 0
        
        # padding at the top and at the side
        pSide = int(regex.group(2))
        pTop = int(regex.group(3))
        
        columns = int(regex.group(4))
        lines = int(regex.group(5))

        for j in range(pTop, pTop+lines):
            for k in range(pSide, pSide+columns):
                if (matrix[j,k] != 0):
                    overlap[id] += 1
                    overlap[matrix[j,k]] += 1
                
                matrix[j,k] = id

    
    for v in overlap:
        if overlap[v] == 0:
            print(v)
            break