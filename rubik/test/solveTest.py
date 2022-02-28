import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solve_01_rotateF(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))