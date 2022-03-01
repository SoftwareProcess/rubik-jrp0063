import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):

    def test_cube_01_cuberead(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        test_cube = cube(cube_str)
        self.assertEqual(cube_str, str(test_cube))