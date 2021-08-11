#!/usr/bin/python

import sys
from os import walk

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

path = sys.argv[1]
print('path=', path)

f = []
for (filenames) in walk(path):
    f.extend(filenames)
    break

# 0 = chemin, 1 = tableau des dossier, 2 = fichier du chemin
print('walk=', str(f))


