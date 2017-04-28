import pdb
import numpy as np
from linearProgram import LinearProgram

type = 'min'
obj1 = np.array([ [1],[1], [-4], [-9] ])
matrix1 = np.array([ [-1,0,2,5], [2,-3,4,-3] ])
ineq1 = np.array([ ['&le;'], ['&ge;'], ['&ge;'], ['='] ])
b1 = np.array([ [10,5] ])
vars1 = np.array([ ['&ge; 0'], ['free'], ['free'], ['&le; 0'] ])
LP1 = LinearProgram(type, obj1, matrix1, ineq1, b1, vars1)
def sef(lp):
    #pdb.set_trace()

    vector_col = lp.obj.shape[0]
    
    #converting obj to be all positive
    if lp.type == 'min':
        for i in range(vector_col):
            if lp.obj[i,0] < 0:
                lp.obj[i,0] = -lp.obj[i,0]

    #LP vars
    m_i = 0
    for i in range(vector_col):
        if lp.vars[i,0] == 'free':
            lp.vars[i,0] = '&ge; 0'
            matrix_col = lp.matrix[:,i]
            for j in range(matrix_col.shape[0]):
                matrix_col[j] = -matrix_col[j]
                
            lp.matrix = np.insert(lp.matrix, m_i, matrix_col, 1)
            m_i = m_i + 1
        m_i = m_i + 1
            
    return [lp.obj, lp.matrix]

print(sef(LP1))
