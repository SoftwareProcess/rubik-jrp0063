import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cube_01_emptycube(self):
        myCube = cube.Cube()
        self.assertIsInstance(myCube, cube.Cube)