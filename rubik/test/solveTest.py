import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solve_01_HAPPY_ValidNominalCube_RotateF(self):
        inputDict = {}
        inputDict['cube'] = ''
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = ''
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))