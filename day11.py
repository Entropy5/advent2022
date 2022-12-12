import numpy as np
import re

# data = open('test.txt', 'r').read().split('\n')
data = open('input11.txt', 'r').read().split('\n')
data = data[:-1]

prop = dict()
logic = dict()
evaluations = dict()
i = 0

while i < len(data):
    if 'Monkey' in data[i]:
        m = int(data[i].split(' ')[1].split(':')[0])
        evaluations[m] = 0
        prop[m] = [int(j) for j in data[i + 1].split(':')[1].split(',')]
        operator, operand = data[i + 2][23:].split(" ")
        operand = int(operand) if 'old' not in operand else 'times self'
        divideby = int(data[i + 3][21:])
        iftrue = int(data[i + 4][29:])
        iffalse = int(data[i + 5][30:])
        logic[m] = (operator, operand, divideby, iftrue, iffalse)
    i += 7

print(logic)
print(prop)
dividebymult = int(np.prod([tup[2] for tup in logic.values()]))
# print("dbm", dividebymult)

for _ in range(10000):
    for m in range(len(prop.keys())):
        operator, operand, divideby, iftrue, iffalse = logic[m]
        while len(prop[m]) > 0:
            evaluations[m] += 1
            worry = prop[m].pop()
            worry = (worry * operand if operand != 'times self' else worry ** 2) if operator == "*" else worry + operand
            # worry = int(worry / 3)
            worry = worry % dividebymult
            prop[iftrue if worry % divideby == 0 else iffalse].append(worry)
    print(prop)

print(evaluations)
sort = sorted(list(evaluations.values()))[::-1]
print(sort[0] * sort[1])
