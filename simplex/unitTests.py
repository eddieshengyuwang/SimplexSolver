from simplex import sef
from linearProgram import LinearProgram
import unittest
import numpy as np

typeMin = 'min'
typeMax = 'max'

obj1 = np.array([[1],[1],[-9]])
matrix1 = np.array([ [-1,0,2], [2,-3,4] ])
ineq1 = np.array([['&le;'], ['=']])
b1 = np.array([[10],[5]])
vars1 = np.array([['free'], ['&le; 0'], ['&ge; 0']])
LP1 = LinearProgram(typeMin, obj1, matrix1,
                    ineq1, b1, vars1)

sol_obj1 = np.array([[1],[-1],[-1],[-9],[0]])
sol_matrix1 = np.array([ [-1,1,0,2,1], [2,-2,3,4,0] ])
sol_ineq1 = np.array([['='], ['=']])
sol_b1 = np.array([[10],[5]])
sol_vars1 = np.array([['&ge; 0'], ['&ge; 0']])
sol_LP1 = LinearProgram(typeMax, sol_obj1, sol_matrix1,
                        sol_ineq1, sol_b1, sol_vars1)

obj2 = np.array([[3], [2], [-1], [1]])
matrix2 = np.array([[1, 2, 1, -1],
                    [-2, -4, 1, 1],
                    [-2, -4, 1, 1]])
ineq2 = np.array([['&le;'], ['&le;']])
b2 = np.array([[5],[-1]])
vars2 = np.array([['%ge; 0'], ['%le; 0']])

class TestSEF(unittest.TestCase):
    def setUp(self):
        self.typeMin = typeMin
        self.typeMax = typeMax
        
        self.obj1 = obj1
        self.matrix1 = matrix1
        self.ineq1 = ineq1
        self.b1 = b1
        self.vars1 = vars1
        self.LP1 = LinearProgram(self.typeMax, self.obj1, self.matrix1,
                                 self.ineq1, self.b1, self.vars1)
        
        self.sol_obj1 = np.array([[1],[-1],[-1],[-9],[0]])
        self.sol_matrix1 = np.array([ [-1,1,0,2,1], [2,-2,3,4,0] ])
        self.sol_ineq1 = np.array([['='], ['=']])
        self.sol_b1 = np.array([[10],[5]])
        self.sol_vars1 = np.array([['&ge; 0'], ['&ge; 0']])
        self.sol_LP1 = LinearProgram(self.typeMax, self.sol_obj1, self.sol_matrix1,
                                     self.sol_ineq1, self.sol_b1, self.sol_vars1)
        
        self.obj2 = obj2
        self.matrix2 = matrix2
        self.ineq2 = ineq2
        self.b2 = b2
        self.vars2 = vars2
        self.LP2 = LinearProgram(self.typeMax, self.obj2, self.matrix2,
                                 self.ineq2, self.b2, self.vars2)
    def sef_equal(self, LP1, LP2):
        test = np.testing.assert_equal(LP1.obj, LP2.obj)
        test = test and np.testing.assert_equal(LP1.matrix, LP2.matrix)
        test = test and np.testing.assert_equal(LP1.ineq, LP2.ineq)
        test = test and np.testing.assert_equal(LP1.b, LP2.b)
        test = test and np.testing.assert_equal(LP1.vars, LP2.vars)
        return test 
    
    def test_sef1(self):
        newLP = sef(self.LP1)
        self.sef_equal(newLP, self.sol_LP1)
    
##    def algo(linearProgram, soln):
##        self.assetEqual(simplex(linearProgram), soln)

if __name__ == '__main__':
    unittest.main(exit=False)
