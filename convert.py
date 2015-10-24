#!/usr/bin/env python3

import pickle

sentences = []
labels = []

iLine = 0
for line in open("2015-10-01-False-SAT"):
    if 0 == (iLine % 100000):
        print("... %d" % iLine)

    parts = line.split("\t")
    
    labels.append( int(parts[1]) )

    sentence = []
    sites = parts[2].split("*")
    for site in sites:
        siteParts = site.split("|")
        if 3 == len(siteParts):
            sentence.append(int(siteParts[0]))
    sentences.append(sentence)

    iLine += 1

data = {}
data["sentences"] = sentences
data["labels"] = labels

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
