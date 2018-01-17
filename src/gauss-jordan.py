#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/geravm
# https://github.com/poncho128
import numpy

col = 0
size = 3

with open('wololo.txt') as f:
    wololo = (line for line in f if not line.startswith('#'))
    matrix = numpy.loadtxt(wololo, dtype='float', delimiter=',', skiprows=1)

    int1 = numpy.shape(matrix)


    inverseMatrix = numpy.identity(int1[0])


def gJordan():
    if(numpy.linalg.det(matrix) !=0):
        print "Determinant is", numpy.linalg.det(matrix),", inverse can be found"
        for col in range (0, size):
            if matrix[col][col] != 1:
                definePivot(col)
            if matrix[col][col] == 1:
                for row in range (0, size):
                    if row != col:
                        if matrix[row][col] != 0:
                            rowAddition(row,col,-matrix[row][col])

        for printedRow in range (0, size):
            print inverseMatrix[printedRow]
    else:
        print "Determinant is 0, no inverse can be found, singular matrix."

def definePivot(row):
    if matrix[row][row] == 0:
        offset = 1
        while matrix[row][row] == 0:
            rowAddition(row,row + offset,1)
            offset = offset + 1
    if matrix[row][row] != 1:
        rowMultiplication(row,1 / matrix[row][row])

def rowMultiplication(changingRow, numToMultiply):

    for currCol in range (0, size):
        matrix[changingRow][currCol] = matrix[changingRow][currCol] * numToMultiply
        inverseMatrix[changingRow][currCol] = inverseMatrix[changingRow][currCol] * numToMultiply

def rowAddition(changingRow, changerRow, numToMultiply):

    for currCol in range (0, size):
        matrix[changingRow][currCol] = matrix[changingRow][currCol] + (matrix[changerRow][currCol]*numToMultiply)
        inverseMatrix[changingRow][currCol] = inverseMatrix[changingRow][currCol] + (inverseMatrix[changerRow][currCol]*numToMultiply)

gJordan()
