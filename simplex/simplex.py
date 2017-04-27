import pdb
import numpy as np
from linearProgram import LinearProgram

type = 'min'
obj1 = np.array([ [1],[1],[-9] ])
matrix1 = np.array([ [-1,0,2], [2,-3,4] ])
ineq1 = np.array([ ['&le;'], ['&ge;'], ['='] ])
b1 = np.array([ [10,5] ])
vars1 = np.array([ ['&ge; 0'], ['free'], ['&le; 0'] ])
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
    for i in range(vector_col):
        if lp.vars[i,0] == 'free':
            lp.vars[i,0] = '&ge; 0'
            matrix_col = matrix[: i]
            for j in range(matrix_col.shape[1]):
                matrix_col[0,j] = -matrix_col[0,j]
                
            np.insert(matrix, 
            
    return lp.obj

print(sef(LP1))
