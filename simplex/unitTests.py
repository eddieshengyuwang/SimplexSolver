from simplex import sef, print_sef
from linearProgram import LinearProgram
import unittest
import numpy as np

np.set_printoptions(threshold=np.nan)

typeMin = 'min'
typeMax = 'max'

obj1 = np.array([[1],[1],[-9]])
matrix1 = np.array([ [-1,0,2], [2,-3,4] ])
ineq1 = np.array([['&le;'], ['=']])
b1 = np.array([[10],[5]])
vars1 = np.array([['free'], ['&le; 0'], ['&ge; 0']])
LP1 = LinearProgram(typeMax, obj1, matrix1,
                    ineq1, b1, vars1)

sol_obj1 = np.array([[1],[-1],[-1],[-9],[0]])
sol_matrix1 = np.array([ [-1,1,0,2,1], [2,-2,3,4,0] ])
sol_ineq1 = np.array([['='], ['=']])
sol_b1 = np.array([[10],[5]])
sol_vars1 = np.array([['&ge; 0'], ['&ge; 0'], ['&ge; 0'], ['&ge; 0'], ['&ge; 0']])
sol_LP1 = LinearProgram(typeMax, sol_obj1, sol_matrix1,
                        sol_ineq1, sol_b1, sol_vars1)

#----------------------------------------------------------------------

obj2 = np.array([[3], [2], [-1], [1]])
matrix2 = np.array([[1, 2, 1, -1],  
                    [-2, -4, 1, 1]])
ineq2 = np.array([['&le;'], ['&le;']])
b2 = np.array([[5],[-1]])
vars2 = np.array([['%ge; 0'], ['%le; 0']])
LP2 = LinearProgram(typeMax, obj2, matrix2, ineq2, b2, vars2)

#sol_obj2 = np.array()

#----------------------------------------------------------------------
obj3 = np.array([[1],[1],[-4],[-9]])
matrix3 = np.array([[-1,0,2,5],
                    [2,-3,4,-3],
                    [-1,9,-5,7],
                    [-1,-3,4,-9]])
ineq3 = np.array([['&le;'], ['&ge;'], ['&ge;'], ['=']])
b3 = np.array([[10],[5],[-7],[0]])
vars3 = np.array([['&ge; 0'], ['free'], ['&le; 0'], ['free']])
LP3 = LinearProgram(typeMin, obj3, matrix3,
                    ineq3, b3, vars3)

sol_obj3 = np.array([[-1],[-1],[1],[-4],[9],[-9],[0],[0],[0]])
sol_matrix3 = np.array([[-1,0,0,-2,5,-5,1,0,0],
                        [2,-3,3,-4,-3,3,0,-1,0],
                        [-1,9,-9,5,7,-7,0,0,-1],
                        [-1,-3,3,-4,-9,9,0,0,0]])
sol_ineq3 = np.array([['='], ['='], ['='], ['=']])
sol_b3 = np.array([[10],[5],[-7],[0]])
sol_vars3 = np.array([['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0']])
sol_LP3 = LinearProgram(typeMax, sol_obj3, sol_matrix3,
                        sol_ineq3, sol_b3, sol_vars3)

class TestSEF(unittest.TestCase):

    def sef_equal(self, LP1, LP2):
#        yo1 = LP1
#        yo2 = LP2
        np.testing.assert_equal(LP1.obj, LP2.obj)
        np.testing.assert_equal(LP1.matrix, LP2.matrix)
        np.testing.assert_equal(LP1.ineq, LP2.ineq)
        np.testing.assert_equal(LP1.b, LP2.b)
        np.testing.assert_equal(LP1.vars, LP2.vars)
    
    def test_sef1(self):
        newLP1 = sef(LP1)
        self.sef_equal(newLP1, sol_LP1)     

    def test_sef2(self):
        newLP3 = sef(LP3)
        self.sef_equal(newLP3, sol_LP3)
    
#        print("old: \n")
#        print_sef(newLP3)
#        print("\n new: \n")
#        print_sef(newLP3)
##    def algo(linearProgram, soln):
##        self.assetEqual(simplex(linearProgram), soln)

if __name__ == '__main__':
    unittest.main(exit=False)
