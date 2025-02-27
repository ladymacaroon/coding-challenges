import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
letters = []
length = len(letters)
             
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    for x in range(len(line)):
        letters.append(line[x])

    for x in range(length):
        if letters[x] == " ":
            letters.pop(x)
    
    print(letters)