import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    total = 0

    # total += line.count('a')
    # total += line.count('e')
    # total += line.count('i')
    # total += line.count('o')
    # total += line.count('u')

    total = sum(map(line.count,['a','e','i','o','u']))

    print(total)