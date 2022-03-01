import unittest
from rubik.cube import Cube

class CubeTest(unittest.TestCase):

    def test_cube_01_cuberead(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cubetest = Cube(cube_str)
        self.assertEqual(cube_str, str(cubetest))