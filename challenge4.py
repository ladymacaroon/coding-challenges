import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    words = line.split('|')
    anagram = sorted(words[1])
    word = sorted(words[0])

    if anagram == word:
        print(f'{line} = ANAGRAM')
    else:
        print(f'{line} = NOT AN ANAGRAM')