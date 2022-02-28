import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solve_01_rotateF(self):
        parm = {'op':'solve', 'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'rotate':'F'}
        result = solve._solve(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')
        cube = result.get('cube')
        self.assertEqual(cube, 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
        print("ST 01 PASSED - rotate F")