import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    coordinates = list(line.split(' '))
    
    for x in range(3):
        coordinates.append(coordinates[x] * 100)
    
    print(coordinates)
    
    # new_coordinates = []

    # for x in range(3):
    #     new_coordinates.append(x, coordinates[x - 180.00])