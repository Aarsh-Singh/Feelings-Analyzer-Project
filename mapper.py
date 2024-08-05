#!/usr/bin/env python3
import json, sys, re

ENGLISH_DICT = "dic.txt"
STATES_FILE = "states"

dictionary = {}
states_arr = []

def loadDictionary(nameFile):
    with open(nameFile) as file:
        for line in file:
            x = line.split("\t")
            dictionary[x[0]] = x[1]

def loadStates():
    with open(STATES_FILE) as file:
        for state in file:
            s = state.split(",")[-1].split()[0]
            states_arr.append(s)

def isState(state):
    return state in states_arr

def sanitizeString(string):
    return re.sub('[^A-Za-z0-9]+', '', string)

def calculateScore(text):
    score = 0
    words = text.split()
    for w in words:
        try:
            w = sanitizeString(w.lower())
            score += int(dictionary[w])
        except:
            pass
    return score

def main():
    for line in sys.stdin:
        jsonLine = json.loads(line)
        key = jsonLine["place"]["full_name"].split()[-1]
        if isState(key):
            value = calculateScore(jsonLine["text"])
            print('%s\t%s' % (key,value))

if __name__ == '__main__':

    ## Load data
    loadDictionary(ENGLISH_DICT)
    loadStates()
    
    main()