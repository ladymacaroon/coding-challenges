import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    animals = line.split(' ')
    turkeys = int(animals[0]) *  2
    goats = int(animals[1]) * 4
    horses = int(animals[2]) * 4

    print(turkeys + goats + horses)