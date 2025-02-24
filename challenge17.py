import sys
import math
import string
from functools import cmp_to_key

def compare_ships(ship1, ship2):
    if ship1[0] < ship2[0]:
        return -1
    elif ship1[0] > ship2[0]:
        return 1
    else:
        if ship1[1] > ship2[1]:
            return -1
        elif ship1[1] < ship2[1]:
            return 1
        else:
            return 0



sections = int(sys.stdin.readline().rstrip())

for section in range(sections):
    cases = int(sys.stdin.readline().rstrip())
    all_coordinates = []

    for caseNum in range(cases):
        line = sys.stdin.readline().rstrip()

        classes = line.split(':')
        ship_type = classes[0]
        coordinates = list(map(int, classes[1].split(',')))
        all_coordinates.append(coordinates)

    sorted_coordinates = sorted(all_coordinates, key=cmp_to_key(compare_ships))
    print(sorted_coordinates)
