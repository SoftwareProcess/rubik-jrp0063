import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):
    
    def test_solve_01_emptycube(self):
        parm = {'op': 'solve'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)