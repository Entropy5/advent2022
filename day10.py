import numpy as np
import re

# data = open('test.txt', 'r').read().split('\n')
data = open('input10.txt', 'r').read().split('\n')
data = data[:-1]

realx = 1
tempx = 1
cycle = 1
signalsum = 0
line = list('_' * 40)
screen = []


def tick():
    global signalsum, cycle
    signal = cycle * realx
    print(f"Cycle {cycle} - TempX {tempx} - RealX {realx} - Signal {signal}")
    line[cycle - 1] = '#' if cycle in (realx, realx + 1, realx + 2) else '.'
    if cycle % 40 == 0:
        screen.append(line.copy())
        cycle -= 40
    if cycle in {20, 60, 100, 140, 180, 220}:
        signalsum += signal
    cycle += 1


for d in data:
    print(d)
    if d == 'noop':
        tick()
    elif 'addx' in d:
        tempx += int(d.split(' ')[1])
        tick()
        tick()
    realx = tempx

print(signalsum)
for s in screen:
    print(''.join(s))
