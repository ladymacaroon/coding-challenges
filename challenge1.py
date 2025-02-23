import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    
    numbers = list(map(float, line.split(":")))

    if math.isclose(numbers[0], 0):
        print("SAFE")
    else:
        collisionTime = numbers[1] / numbers[0]

        if collisionTime <= 1.0:
            print("SWERVE")
        elif collisionTime <= 5.0:
            print("BRAKE")
        else:
            print("SAFE")