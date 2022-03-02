import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):
    
    def test_solve_01_emptycube(self):
        parm = {'op': 'solve'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)
    
    @unittest.skip('error messages incomplete')
    def test_solve_02_badcube(self):
        parm = {'op': 'solve',
                'cube': 9}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)
    
    @unittest.skip('error messages incomplete')
    def test_solve_03_rotate_notstring(self):
        parm = {'op': 'solve',
                'rotate': 9,
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)
    
    @unittest.skip('error messages incomplete')
    def test_solve_04_rotate_notletter(self):
        parm = {'op': 'solve',
                'rotate': '9',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)
    
    #@unittest.skip('cube rotate incomplete')
    def test_solve_05_rotate_empty(self):
        parm = {'op': 'solve',
                'rotate': '',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        cube = result.get('cube')
        self.assertEqual(cube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
    
    #@unittest.skip('cube rotate incomplete')
    def test_solve_06_rotate_missing(self):
        parm = {'op': 'solve',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        cube = result.get('cube')
        self.assertEqual(cube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
    
    #@unittest.skip('error messages incomplete')
    def test_solve_07_rotate_invalidchars(self):
        parm = {'op': 'solve',
                'rotate': 'x',
                'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)
    
    #@unittest.skip('cube rotate incomplete')
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
        