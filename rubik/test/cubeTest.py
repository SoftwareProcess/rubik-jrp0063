import unittest
from rubik.cube import Cube

class CubeTest(unittest.TestCase):

    # @unittest.skip('cube rotate incomplete')
    def test_cube_01_cuberead(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        self.assertEqual(cube_str, str(cube))
        
    @unittest.skip('cube rotate incomplete')
    def test_cube_02_cuberotate_F(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('F')
        self.assertEqual(str(cube), 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
        
    @unittest.skip('cube rotate incomplete')
    def test_cube_03_cuberotate_f(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('f')
        self.assertEqual(str(cube), 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy')