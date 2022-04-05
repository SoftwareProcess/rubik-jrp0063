import unittest
from rubik.cube import Cube

class CubeTest(unittest.TestCase):

    def test_cube_01_read(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        self.assertEqual(cube_str, str(cube))
    
    #@unittest.skip
    def test_cube_02_rotate_F(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('F')
        self.assertEqual(str(cube), 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
    
    #@unittest.skip
    def test_cube_03_rotate_f(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('f')
        self.assertEqual(str(cube), 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy')
    
    #@unittest.skip
    def test_cube_04_rotate_R(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('R')
        self.assertEqual(str(cube), 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb')
    
    #@unittest.skip    
    def test_cube_05_rotate_r(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('r')
        self.assertEqual(str(cube), 'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg')
        
    #@unittest.skip    
    def test_cube_06_rotate_B(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('B')
        self.assertEqual(str(cube), 'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo')
        
    #@unittest.skip    
    def test_cube_07_rotate_b(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('b')
        self.assertEqual(str(cube), 'gggggggggrrwrrwrrwbbbbbbbbbyooyooyooooowwwwwwyyyyyyrrr')
        
    #@unittest.skip    
    def test_cube_08_rotate_L(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('L')
        self.assertEqual(str(cube), 'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy')
        
    #@unittest.skip    
    def test_cube_09_rotate_l(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('l')
        self.assertEqual(str(cube), 'yggyggyggrrrrrrrrrbbwbbwbbwooooooooogwwgwwgwwbyybyybyy')
        
    #@unittest.skip    
    def test_cube_10_rotate_U(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('U')
        self.assertEqual(str(cube), 'rrrggggggbbbrrrrrrooobbbbbbgggoooooowwwwwwwwwyyyyyyyyy')
        
    #@unittest.skip    
    def test_cube_11_rotate_u(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('u')
        self.assertEqual(str(cube), 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy')
        
    #@unittest.skip    
    def test_cube_12_rotate_D(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('D')
        self.assertEqual(str(cube), 'ggggggooorrrrrrgggbbbbbbrrroooooobbbwwwwwwwwwyyyyyyyyy')
        
    #@unittest.skip    
    def test_cube_13_rotate_d(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('d')
        self.assertEqual(str(cube), 'ggggggrrrrrrrrrbbbbbbbbbooooooooogggwwwwwwwwwyyyyyyyyy')
        
    #@unittest.skip
    def test_cube_14_rotate_all(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        for rotation in 'FRUBLDfrubld':
            cube.rotate(rotation)
        self.assertEqual(str(cube), 'wwgogwwgwwyrbrbbrbyyyybrobyggowobgogoobwwrbooryrgygrry')
        
    @unittest.skip
    def test_cube_15_daisy_solve_solved(self):
        cube_str = 'rborbbwbrbrrrrobrgggbggywbooowooyggowwywywbwygoyywgyyr'
        cube = Cube(cube_str)
        cube.makeDaisy()
        test = str(cube)
        petal_color = [test[49], test[49], test[49], test[49]]
        petals = [test[43], test[39], test[37], test[41]]
        self.assertEqual(petal_color, petals)
        self.assertEqual(str(cube), 'rborbbwbrbrrrrobrgggbggywbooowooyggowwywywbwygoyywgyyr')
        
    @unittest.skip    
    def test_cube_16_daisy_solve_unsolved(self):
        cube_str = 'boorbrbgwygbyrwgyrowgrgobbgyyogobwywrbwbyrywgrwogworoy'
        cube = Cube(cube_str)
        cube.makeDaisy()
        test = str(cube)
        test_color = [test[49], test[49], test[49], test[49]]
        petals = [test[43], test[39], test[37], test[41]]
        self.assertEqual(test_color, petals)
    
    @unittest.skip
    def test_cube_17_bottomcross_solve_solved(self):
        cube_str = 'wgorooborbbgybygbrogwrrgbrroooygbygwgrybyyboyrwwwwwgwy'
        cube = Cube(cube_str)
        cube.makeBottomCross()
        test = str(cube)
        test_cross = [test[49], test[49], test[49], test[49]]
        bottom_cross = [test[46], test[50], test[52], test[48]]
        self.assertEqual(test_cross, bottom_cross)
    
    @unittest.skip
    def test_cube_18_bottomcross_solve_unsolved(self):
        cube_str = 'brrrorrbybogybogrwogryrogbbyboggbwgwbwywywywwgorywgoyo'
        cube = Cube(cube_str)
        cube.makeBottomCross()
        test = str(cube)
        test_cross = [test[49], test[49], test[49], test[49]]
        bottom_cross = [test[46], test[50], test[52], test[48]]
        self.assertEqual(test_cross, bottom_cross)
        