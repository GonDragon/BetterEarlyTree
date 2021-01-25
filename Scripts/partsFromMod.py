import os
import sys
import pathlib

moddir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

parts = {}

# r = root, d = directories, f = files
for r, d, f in os.walk(moddir):
    for file in f:
        if file.endswith(".cfg"):
            parts[file] = os.path.join(r, file)


for k, v in parts.items():
    print('{0} : {1}'.format(k, v))
    with open(v, 'r') as cfgFile:
        print(' '.join(cfgFile.readlines()))
