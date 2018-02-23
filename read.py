import numpy as np

def readFile(filename: object, dSimplex: object) -> object:
    file = open(filename)
    dims = file.readline()
    config = {}
    for pair in dims.split(';'):
        key = pair.split("=")[0].strip()
        value = int(pair.split('=')[1].strip())
        config[key] = value
    dSimplex.n = config['n']
    dSimplex.m = config['m']
    dSimplex.matrixA = np.zeros(dSimplex.m * dSimplex.n).reshape(dSimplex.m, dSimplex.n)
    dSimplex.vecB = np.zeros(dSimplex.m)
    dSimplex.vecC = np.zeros(dSimplex.n)
    for i in range(0, dSimplex.m):
        line = file.readline()
        elem = line.split(' ')
        for j in range(0, dSimplex.n):
            dSimplex.matrixA[i][j] = int(elem[j].strip())
        dSimplex.unequals.append(elem[dSimplex.n])
        dSimplex.vecB[i] = int(elem[dSimplex.n + 1])
    task = file.readline()
    elem = task.split(' ')

    for i in range(0, dSimplex.n):
        dSimplex.vecC[i] = int(elem[i].strip())

    limits = file.readline().split(' ')
    for ind in limits:
        dSimplex.varLim.append(int(ind) - 1)
    file.close()


def initStartVecTask(dCanon, startOpVec):
    startOpVec.m = dCanon.m
    startOpVec.vecB = dCanon.vecB
    startOpVec.n = dCanon.m + dCanon.n
    matrixY = np.eye(startOpVec.m)
    vecY = np.ones(startOpVec.m)
    matrixC = matrixY * vecY
    startOpVec.matrixA = dCanon.matrixA
    for i in range(0, startOpVec.m):
       startOpVec.matrixA = np.c_[startOpVec.matrixA, matrixC[:,i]]
    for i in range(0, startOpVec.m):
        if startOpVec.vecB[i] < 0:
            startOpVec.vecB[i] *=-1
            for j in range(0, startOpVec.n):
                startOpVec.matrixA[i][j] *=-1
    startOpVec.startVec = np.zeros(startOpVec.n + startOpVec.m)
    for i in range(0, startOpVec.m):
        startOpVec.startVec[startOpVec.n + i] = startOpVec.vecB[i]
    startOpVec.startVec = startOpVec.startVec.reshape(startOpVec.n + startOpVec.m,1)
