# sides are read in this order from sequence
SIDES = ('front', 'right', 'back', 'left', 'up', 'down')



class Cube:
    
    
    def __init__(self, cube_str: str):
        #self.cube_str = cube_str
        self.faces = {
            face: [
                [cube_str[offset + 0], cube_str[offset + 1], cube_str[offset + 2]],
                [cube_str[offset + 3], cube_str[offset + 4], cube_str[offset + 5]],
                [cube_str[offset + 6], cube_str[offset + 7], cube_str[offset + 8]],
                ]
            for face, offset in zip(SIDES, (0, 9, 18, 27, 36, 45))
            }
        
        
    def __getitem__(self, item: int) -> str:
        return self.faces[SIDES[item // 9]][item % 9 // 3][item % 3]
    
    def show(self):
        print(self.cube_str)
        
#testcube = Cube('gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy')
#testcube.show()