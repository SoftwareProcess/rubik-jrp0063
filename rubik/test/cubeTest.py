import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):

    def test_cube_01_emptycube(self):
        myCube = cube.Cube()
        self.assertIsInstance(myCube, cube.Cube)