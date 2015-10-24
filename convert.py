#!/usr/bin/env python3

import pickle
import argparse
import random

parser = argparse.ArgumentParser(description="prepare data for serps modeling")
parser.add_argument('-l', "--limit", type=int, help="limir", default=max)

args = parser.parse_args()

limit = args.limit

dictionary = {}
dictionary[0] = "<UNK>"
index = 1
for line in open("2015-10-01-False-TopHosts2"):
    parts = line.split("\t")
    dictionary[index] = parts[0]
    index += 1

train_x = []
train_y = []
test_x = []
test_y = []

iLine = 0
for line in open("2015-10-01-False-SAT"):
    if 0 == (iLine % 100000):
        print("... %d" % iLine)

    if iLine > limit:
        break

    parts = line.split("\t")
    
    label = int(parts[1])

    sentence = []
    sites = parts[2].split("*")
    for site in sites:
        siteParts = site.split("|")
        if 3 == len(siteParts):
            sentence.append(int(siteParts[0]))
    sentences.append(sentence)

    if random.randint(0, 10) < 8:
        train_x.append(sentence)
        train_y.append(label)
    else:
        test_x.append(sentence)
        test_y.append(label)

    iLine += 1
    
with open("data.pkl", "wb") as f:
    pkl.dump((train_x, train_y), f, -1)
    pkl.dump((test_x, test_y), f, -1)

    revDict = {}
    for k, v in dictionary.items():
        revDict[v] = k
    pkl.dump(revDict, f, -1)
