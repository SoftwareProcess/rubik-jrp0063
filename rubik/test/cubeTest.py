import unittest
from rubik.cube import Cube

class CubeTest(unittest.TestCase):

    def test_cube_01_cuberead(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        test_cube = Cube(cube_str)
        self.assertEqual(cube_str, str(test_cube))
        
    @unittest.skip('cube rotate incomplete')
    def test_cube_02_cuberotate_F(self):
        pass