import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    words = line.split('|')
    anagram = words[1]
    word = words[0]
    correct = True

    for x in range(len(anagram)):
        if anagram[x].find(word[x]) != -1:
            correct = True
        else:
            correct = False

    if correct == True:
        print(f'{line} =ANAGRAM')
    else:
        print(f'{line} =NOT AN ANAGRAM')