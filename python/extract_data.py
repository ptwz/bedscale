import shelve
from collections import OrderedDict
from itertools import combinations

import time

with open('waage.log','r') as file:
        raw = file.readlines()

raw = [ l.strip().split() for l in raw]

timeline = OrderedDict([ (float(l[0]),float(l[2]) ) for l in raw ])

bins = shelve.open("people.shelve")

to_try = []
for l in range(1,len(bins)+1):
    to_try += [x for x in combinations(bins, l)]

for time in timeline:
    # Try all combinations out
    step = abs(timeline[time])
    deltas = OrderedDict()
    sums={}
    for c in to_try:
        s=sum([ bins[key] for key in c])
        sums[c] = s
        deltas[c] = abs(s-step)
    # Sort deltas by value
    deltas=OrderedDict(sorted(deltas.iteritems(), key=lambda x: x[1]))
    nearest = deltas.keys()[0]
    if abs(deltas[nearest]) > 0.03*sums[nearest] or abs(deltas[nearest]) > .5:
        continue
    if len(nearest)==1:
        # Update matching weight
        name = nearest[0]
        bins[name] = step
        print time, name, step
    else:
        for name in nearest:
            if step>0:
                bins[name] += deltas[nearest] / len(nearest)
            else:
                bins[name] -= deltas[nearest] / len(nearest)
            print time, name, bins[name]

