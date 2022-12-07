import numpy as np
import re

# data = open('test7.txt', 'r').read().split('\n')
data = open('input7.txt', 'r').read().split('\n')
allfolders = set()


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = dict()
        allfolders.add(self)

    def getsize(self):
        total = 0
        for c in self.children.values():
            if type(c) == Folder:
                total += c.getsize()
            else:
                total += c
        return total

    def __str__(self):
        return f"{self.name}:[{[str(k) for k in self.children.keys()]}]"


system = Folder('system', None)
i = 0
target = system

while i < len(data):
    command = data[i]
    if 'cd' in command:
        if command == '$ cd /':
            target = system
        elif command == '$ cd ..':
            target = target.parent
        else:
            target = target.children[command[5:]]
    elif command == '$ ls':
        i += 1
        while '$' not in data[i] and data[i] != '':
            command = data[i]
            if 'dir' in command:
                target.children[command[4:]] = Folder(command[4:], target)
            else:
                size, name = command.split(' ')
                target.children[name] = int(size)
            i += 1
        continue

    i += 1

print(system)

bigtotal = 0
for f in allfolders:
    s = f.getsize()
    if s < 100000:
        bigtotal += s
print(bigtotal)

needed = 30000000 - 70000000 + system.getsize()
print(min([f.getsize() for f in allfolders if needed <= f.getsize()]))
