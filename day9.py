import numpy as np
import re

# data = open('test9.txt', 'r').read().split('\n')
data = open('input9.txt', 'r').read().split('\n')
data = data[:-1]

head = np.array([0, 0])
tail = np.array([0, 0])
length = 10
rope = np.zeros((length, 2), dtype=int)

visited = set()
moving = dict({'U': np.array([0, 1]), 'D': np.array([0, -1]), 'L': np.array([-1, 0]), 'R': np.array([1, 0])})

for d in data:
    direc, num = d.split(' ')
    for i in range(int(num)):
        rope[0] += moving[direc]  # move head
        for j in range(1, length):  # iterate over rope
            if rope[j - 1][0] == rope[j][0] and abs(rope[j - 1][1] - rope[j][1]) == 2:
                # move vertical
                rope[j][1] += 1 if rope[j - 1][1] > rope[j][1] else -1
            elif rope[j - 1][1] == rope[j][1] and abs(rope[j - 1][0] - rope[j][0]) == 2:
                # move horizontal
                rope[j][0] += 1 if rope[j - 1][0] > rope[j][0] else -1
            elif rope[j - 1][0] != rope[j][0] and rope[j - 1][1] != rope[j][1] and abs(rope[j - 1][0] - rope[j][0]) + abs(rope[j - 1][1] - rope[j][1]) > 2:
                # move diagonal
                rope[j][0] += 1 if rope[j - 1][0] > rope[j][0] else -1
                rope[j][1] += 1 if rope[j - 1][1] > rope[j][1] else -1
        visited.add(tuple(rope[9]))  # track a specific knot

print(rope)
print(len(visited))
