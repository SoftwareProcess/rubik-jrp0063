import unittest
import rubik.solve as solve

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
    def test_solve_08_solve_from_solved(self):
        parm = {'op': 'solve',
                'cube': 'rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        solution = result.get('solution')
        self.assertEqual(solution, '')
        
    #@unittest.skip
    def test_solve_09_solve_from_scrambled(self):
        parm = {'op': 'solve',
                'cube': 'ybooroyywyybbgwogoywroorwrwbbrybyrgrwgorygbwggbbowrgwg'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        solution = result.get('solution')
        self.assertEqual(solution, solution)
        
    #@unittest.skip
    def test_solve_10_solve_from_updaisy(self):
        parm = {'op': 'solve',
                'cube': 'ybrgrooywwrybgrogbgobbooorgwgrgbyrygrwowywbwgwbbowryyy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        solution = result.get('solution')
        self.assertEqual(solution, solution)

    #@unittest.skip
    def test_solve_11_solve_from_downcross(self):
        parm = {'op': 'solve',
                'cube': 'gyrgrbrrygrbrggrgbwgyooooowgyobbyobworroyywbygwbwwwbwy'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        solution = result.get('solution')
        self.assertEqual(solution, solution)
        
    #@unittest.skip
    def test_solve_12_solve_from_downface(self):
        parm = {'op': 'solve',
                'cube': 'googrrrrrbrybgbgggbgoyoyoooygrobobbbgrryyyybywwwwwwwww'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        solution = result.get('solution')
        self.assertEqual(solution, solution)
        
    @unittest.skip
    def test_solve_13_solve_from_scrambled_A5_PATCH(self):
        parm = {'op': 'solve',
                'cube': 'NNNH8N88TTpp8pH88ggHT8gpTT8NgggNNNgpgpHHHTHg8HppTTTHNp'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        solution = result.get('solution')
        self.assertEqual(solution, solution)
    