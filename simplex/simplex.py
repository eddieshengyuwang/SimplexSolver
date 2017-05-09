import pdb
import numpy as np
from linearProgram import LinearProgram

type = 'min'
obj1 = np.array([ [1],[1], [-4], [-9] ])
matrix1 = np.array([ [-1,0,2,5], [2,-3,4,-3], [-1,9,-5,7], [-1,-3,4,-9] ])
ineq1 = np.array([ ['&le;'], ['&ge;'], ['&ge;'], ['='] ])
b1 = np.array([ [10],[5],[-7],[0] ])
vars1 = np.array([ ['&ge; 0'], ['free'], ['&le; 0'], ['free'] ])
#vars1 = np.array([ ['free'], ['free'], ['free'], ['free'] ])
#vars1 = np.array([ ['free'], ['free'], ['free'], ['free'] ])
LP1 = LinearProgram(type, obj1, matrix1, ineq1, b1, vars1)
def sef(lp):
    #pdb.set_trace();

    c_rows = lp.obj.shape[0]
    m_rows = lp.matrix.shape[0]
    
    #converting obj to be max
    if lp.type == 'min':
        lp.type = 'max'
        for i in range(c_rows):
            if lp.obj[i,0] < 0:
                lp.obj[i,0] = -lp.obj[i,0]
                
    #converting variables <= 0 or free to be >= in vars
    i = c_rows-1
    while i >= 0:
        if lp.vars[i,0] == 'free':
            lp.vars[i,0] = '&ge; 0'
            matrix_col = lp.matrix[:,i]
            new_col = matrix_col.copy()
            for j in range(matrix_col.shape[0]):
               new_col[j] = -matrix_col[j]
               
            lp.matrix = np.insert(lp.matrix, i+1, new_col, 1)           
            lp.obj = np.insert(lp.obj, i+1, -lp.obj[i], 0)
            
        elif lp.vars[i,0] == '&le; 0':
            lp.vars[i,0] = '&ge; 0'
            matrix_col = lp.matrix[:,i]
            for j in range(matrix_col.shape[0]):
                matrix_col[j] = -matrix_col[j]
            lp.obj[i] = -lp.obj[i]
            
        i = i - 1
    
    #converting inequalities >= and <= to be = in ineq
    m = 0
    for i in lp.ineq:
        zero_vector = np.zeros(m_rows)
        if i == '&le;':
            i = '='
            zero_vector[m] = 1
            lp.matrix = np.c_[lp.matrix, zero_vector]
            lp.obj = np.append(lp.obj, [[0]], axis=0)
            m = m + 1
        elif i == '&ge;':
            i = '='
            zero_vector[m] = -1
            lp.matrix = np.c_[lp.matrix, zero_vector]
            lp.obj = np.append(lp.obj, [[0]], axis=0)
            m = m + 1
            
#    print(lp.obj)
#    print(lp.matrix)
#    print(lp.ineq)
#    print(lp.b)
#    print(lp.vars)
    
    return lp

def print_sef(lp):
    print(lp.type)
    print(lp.obj)
    print(lp.matrix)
    print(lp.ineq)
    print(lp.b)
    print(lp.vars)


