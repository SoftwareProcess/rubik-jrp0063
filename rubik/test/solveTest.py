import unittest
import rubik.solve as solve
from rubik.cube import Cube

class SolveTest(unittest.TestCase):
    
    # CHECK TESTS
    
    #@unittest.skip
    def test_solve_01_rotate_missing(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        
    #@unittest.skip    
    def test_solve_02_rotate_empty(self):
        parm = {'op': 'solve',
                'rotate': '',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
    
    #@unittest.skip
    def test_solve_03_rotate_notastring(self):
        parm = {'op':'solve',
                'cube': 9}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: not a string')
    
    #@unittest.skip
    def test_solve_04_rotate_notletter(self):
        parm = {'op': 'solve',
                'rotate': '9',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: must be alphabetical')
    
    #@unittest.skip
    def test_solve_05_rotate_invalidrotationchar(self):
        parm = {'op': 'solve',
                'rotate': 'x',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: invalid rotation character')
    
    #@unittest.skip
    def test_solve_06_rotate_valid(self):
        parm = {'op': 'solve',
                'rotate': 'F',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        cube = result.get('cube')
        self.assertEqual(cube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
        
    #@unittest.skip    
    def test_solve_07_rotate_valid_all(self):
        parm = {'op': 'solve',
                'rotate': 'FRUBLDfrubld',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        cube = result.get('cube')
        self.assertEqual(cube, 'wwgogwwgwwyrbrbbrbyyyybrobyggowobgogoobwwrbooryrgygrry')
        
    #@unittest.skip
    def test_solve_08_bottom_cross_solved(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        solution = result.get('solution')
        self.assertEqual(solution, '')
        
    #@unittest.skip
    def test_solve_09_bottom_cross_fromdaisy(self):
        parm = {'op': 'solve',
                'cube': 'xxLxLLxLLEUUUEEUEExLLxxLxxLUEEEUUEUUttttPtPtPPPPPtPtPt'} 
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        solution = result.get('solution')
        self.assertEqual(solution, 'UUFFRRBBLL')
        
        
        