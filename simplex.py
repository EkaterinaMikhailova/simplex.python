import numpy as np
def updateIndex(suppVec, n):
    k,m = 0
    N_0 = []
    N_plus  = []
    for i in range(0, n):
        if suppVec[i] > 0:
            N_plus.append(i)
        else:
            N_0.append(i)
    return N_0, N_plus

def simplex(sData, startOpVec):
    # проверить определитель
    xNew = np.zeros(sData.newN)
    y = np.zeros(sData.m)
    N_0, N_plus = updateIndex(startOpVec.startVec,startOpVec.newN)
    newA = sData.matrixA
    #фиктивный столбец
    matrix_0 = np.zeros(startOpVec.m, 1)
    for i in range(0, N_0.size):
       matrix_0 = np.c_[matrix_0, startOpVec.matrixA[:,N_0[i]]]
    #удаляем столбец
    matrix_0 = np.delete(matrix_0, 0, 1) #vfdhgd#
    for i in N_0:
        newA = np.delete(newA, i, 1)#&
    m, n  = newA.shape
    if m != n:
        #ДОПОЛНИНЛИ МАТРИЦУ ДО КВАДРАТНОЙ
        for i in range(0, n - m):
            newA = np.c_[newA, matrix_0[:, N_0[i]]]
    np.linalg.det(newA)

