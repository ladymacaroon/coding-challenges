import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    numbers = line.split(" ")
    numbers = list(map(int, numbers))

    addition = numbers[0] + numbers[1]
    multiplication = numbers[0] * numbers[1]

    print(f'{addition} {multiplication}')