import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):

    def test_cube_01_cuberead(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        self.assertEqual(str(cube), cube_str)