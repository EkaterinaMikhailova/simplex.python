from dataSimplex import dataSimplex
from read import readFile

fileName = input('please enter a filename: ')
dSimpl = dataSimplex()

readFile(fileName, dSimpl)
print(dSimpl.n, dSimpl.m)
for i in range(0, dSimpl.m):
    print(dSimpl.matrixA[i][:],dSimpl.unequals[i], dSimpl.vecB[i])
