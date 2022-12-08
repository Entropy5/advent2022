import numpy as np
import re

# data = open('test8.txt', 'r').read().split('\n')
data = open('input8.txt', 'r').read().split('\n')
data = data[:-1]
height, width = len(data), len(data[0])
total = 2 * width + 2 * height - 4

for xi in range(1, width - 1):
    for yi in range(1, height - 1):
        if any([all([data[yi][xi] > data[y][xi] for y in range(yi + 1, height)]),
                all([data[yi][xi] > data[y][xi] for y in range(0, yi)]),
                all([data[yi][xi] > data[yi][x] for x in range(xi + 1, width)]),
                all([data[yi][xi] > data[yi][x] for x in range(0, xi)])]):
            total += 1
print(total)

scenics = []
for xi in range(1, width - 1):
    for yi in range(1, height - 1):
        d1, d2, d3, d4 = 0, 0, 0, 0
        for y in range(yi + 1, height):
            d1 += 1
            if data[yi][xi] <= data[y][xi]:
                break
        for y in range(0, yi)[::-1]:
            d2 += 1
            if data[yi][xi] <= data[y][xi]:
                break
        for x in range(xi + 1, width):
            d3 += 1
            if data[yi][xi] <= data[yi][x]:
                break
        for x in range(0, xi)[::-1]:
            d4 += 1
            if data[yi][xi] <= data[yi][x]:
                break
        scenics.append(d1 * d2 * d3 * d4)
print(max(scenics))
