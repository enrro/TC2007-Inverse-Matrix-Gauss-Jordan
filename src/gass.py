import numpy as np
from numpy.linalg import inv

with open('data.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    MO = np.loadtxt(lines, dtype='i', delimiter=',', skiprows=1)
print("The objective matrix is \n", MO, "\n shape ", np.shape(MO), "\n")
int1 = np.shape(MO)


MI = np.identity(int1[0])
print("The identity matrix of this problem is \n", MI, "\n")

detM = np.linalg.det(MO)

print("The determinant is ", detM, "\n")


if detM == 0:
    print("This is a singular matrix.")
    exit()


print(MO)

ainv = inv((MO))
print("inverse matrix \n", ainv)
