from simplex import sef
from linearProgram import LinearProgram
import unittest
import numpy as np

class TestSEF(unittest.TestCase):
    def setUp(self):
        self.typeMin = 'min'
        self.typeMax = 'max'
        self.obj1 = np.array([[1,1,-9]])
        self.matrix1 = np.array([ [-1,0,2], [2,-3,4] ])
        self.ineq1 = np.array(['&le;', '&ge;', '='])
        self.b1 = np.array([10])
        self.vars1 = np.array(['&ge; 0', 'free', '&le; 0'])
        self.LP1 = LinearProgram(self.typeMin, self.obj1, self.matrix1,
                                 self.ineq1, self.b1, self.vars1)

    def test_sef1(self):
        np.testing.assert_equal(self.LP1.obj, self.obj1)
        
##    def algo(linearProgram, soln):
##        self.assetEqual(simplex(linearProgram), soln)

if __name__ == '__main__':
    unittest.main(exit=False)
