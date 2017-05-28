import pdb
import numpy as np
from linearProgram import LinearProgram

np.set_printoptions(threshold=np.nan)

obj3 = np.array([[-8],[-10],[-7]])
matrix3 = np.array([[1,3,2],
                    [-1,-5,-1]])
ineq3 = np.array([['&le;'], ['&ge;']])
b3 = np.array([[10],[-8]])
vars3 = np.array([['&ge; 0'], ['&ge; 0'], ['&ge; 0']])
LP3 = LinearProgram('min', obj3, matrix3,
                    ineq3, b3, vars3)

def sef(lp):
    #pdb.set_trace();

    c_rows = lp.obj.shape[0]
    m_rows = lp.matrix.shape[0]
    
    #converting obj to be max
    if lp.type == 'min':
        lp.type = 'max'
        for i in range(c_rows):
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
            lp.vars = np.insert(lp.vars, i+1, '&ge; 0', 0)
            
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
        if i != '=':
            if i == '&le;':
                zero_vector[m] = 1
            else:
                zero_vector[m] = -1
            lp.matrix = np.c_[lp.matrix, zero_vector]
            lp.obj = np.append(lp.obj, [[0]], axis=0)
            lp.vars = np.append(lp.vars, [['&ge; 0']], axis=0)
            m = m + 1    
            
    for i in range(m_rows):
        lp.ineq[i,0] = '='
            
    return lp

def print_lp(lp):
    print(lp.type)
    print(lp.obj)
    print(lp.matrix)
    print(lp.ineq)
    print(lp.b)
    print(lp.vars)  

#def TwoPhase(lp):
#    original_LP = lp
#    
#def checkTwoPhase(lp):
#    lp = sef(lp)
#    c = sum(lp.b.T)
    
    

def simplex(lp):
    v_rows = lp.obj.shape[0]
    v_cols = lp.obj.shape[1]
    
    lp = sef(lp)
    
    m_rows = lp.matrix.shape[0]
    m_cols = lp.matrix.shape[1]
    
    #making b matrix all positive
    for i in range(m_rows):
        if lp.b[i,0] < 0:
            lp.b[i,0] = -lp.b[i,0]
            lp.matrix[i] = np.negative(lp.matrix[i])
    
    #constructing tableau
    #pdb.set_trace()
    top_tab = np.c_[lp.matrix, np.zeros(m_rows), lp.b]
    lower_tab = np.concatenate((np.negative(lp.obj),[[1],[0]]), axis=0).T
    tab_cols = top_tab.shape[1]
                              
    #while lower_tab has negative entries, meaning not optimal                           
    while np.any([x for x in lower_tab[0] if x < 0]):
        #choose smallest number in lower_tab
        pivotCol = np.argmin(lower_tab)
        col = top_tab[:,pivotCol]
        
        indicator = top_tab[:,-1]/col
        print("indicator: ")
        print(indicator)
        
        #choose smallest, non-negative indicator
        
        positive_indicators = [y for y in indicator if y > 0]
        if (len(positive_indicators) > 0):
            minPositiveIndicator = np.min(positive_indicators)
            pivotRow = np.where(indicator==minPositiveIndicator)[0].shape[0]
            
           
            #pivotVariable corresponds to intersection of smallest, non-neg
            #indicator and smallest number in lower_tab
            pivotVariable = top_tab[pivotRow, pivotCol]
            
            # "row-reducing" according to pivot variable for all other rows in
            # tableau
            top_tab[pivotRow] = top_tab[pivotRow]/pivotVariable
            for i in range(m_rows):
                if i != pivotRow:
                    constant = -top_tab[i, pivotCol]
                    for j in range(tab_cols):
                        top_tab[i,j] = constant*top_tab[pivotRow,j]+top_tab[i,j]
            
            constant = -lower_tab[0, pivotCol]
            for j in range(tab_cols):
                lower_tab[0,j] = constant*top_tab[pivotRow,j]+lower_tab[0,j]
            print(top_tab)
            print(lower_tab)
        #else: unbounded
    
    #optimal value found
    #combine top_tab and lower_tab and iterate through columns to find 
    #basic variables
    
    tableau = np.concatenate((top_tab, lower_tab), axis=0)
    basicVariables = []
    x = 0
    for column in tableau.T:
        checkFor1List = [y for y in column if y == 1]
        if len(checkFor1List) == 1 and sum(column) == 1 and not np.array_equal(column, tableau.T[-1]):
            xValueRow = np.where(column==1)[0][0]
            xValue = tableau.T[-1,xValueRow]
            basicVariables.append((x+1,xValue))
        x = x + 1
    
    print()
    print()
    print(basicVariables)                       
    print(top_tab)
    print(lower_tab)
    #print_lp(lp)
    
simplex(LP3)
#print_sef(sef(LP3))


