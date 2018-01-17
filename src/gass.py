import numpy as np

with open('data.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    FH = np.loadtxt(lines, dtype='i', delimiter=',', skiprows=1)
print(FH)

