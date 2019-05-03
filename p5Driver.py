#!/user/bin/env python3

import os
import sys
from p5Dict import argCheck, parseFile, printtext, printVariables, printLabels, printFile

count=0

def openFile(F):
    global count
    try:
        with open(F, 'r') as FILE:
            for line in FILE:
                parseFile(line, count)
                count +=1
    except Exception as e:
        print(e)
        exit(1)

def main():
    '''main function'''
    argCheck()
    FILE = sys.argv[1]
    openFile(FILE)
    printFile(FILE)
    printVariables()
    printLabels()
    

if __name__ == "__main__":
    main()
