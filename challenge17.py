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
        
def advance_ships(ships):
    for x in range(len(ships)):
        ship = ships[x] 
        match ship[3]:
            case 'A': ship[0] -= 10
            case 'B': ship[0] -= 20
            case 'C': ship[0] -= 30
            case _: print("error")
        ships[x] = ship

sections = int(sys.stdin.readline().rstrip())

for section in range(sections):
    cases = int(sys.stdin.readline().rstrip())
    all_coordinates = []

    for caseNum in range(cases):
        line = sys.stdin.readline().rstrip()

        classes = line.split(':')
        ship_type = list(classes[0].split('_'))
        coordinates = list(map(int, classes[1].split(',')))
        coordinates.append(ship_type[0])
        coordinates.append(ship_type[1])
        all_coordinates.append(coordinates)

    while len(all_coordinates) > 0:
        all_coordinates = sorted(all_coordinates, key=cmp_to_key(compare_ships))
        destroyed_ship = all_coordinates.pop(0)
        print(f"Destroyed Ship: {destroyed_ship[2]} xLoc {destroyed_ship[0]}")
        advance_ships(all_coordinates)
    
    