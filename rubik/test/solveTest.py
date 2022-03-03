import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):
    
    def test_solve_01_rotate_missing(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        cube = result.get('cube')
        self.assertEqual(cube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
        
    def test_solve_02_rotate_empty(self):
        parm = {'op': 'solve',
                'rotate': '',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        cube = result.get('cube')
        self.assertEqual(cube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
    
    def test_check_03_Error_NotAString(self):
        parm = {'op':'solve',
                'cube': 9}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual(status, 'ok')
    
    def test_solve_04_rotate_notletter(self):
        parm = {'op': 'solve',
                'rotate': '9',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)
    
    def test_solve_07_rotate_invalidrotationchars(self):
        parm = {'op': 'solve',
                'rotate': 'x',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)
    
    def test_solve_08_rotate_valid(self):
        parm = {'op': 'solve',
                'rotate': 'F',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        cube = result.get('cube')
        self.assertEqual(cube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
        