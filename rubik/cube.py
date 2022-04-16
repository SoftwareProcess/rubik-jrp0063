
# NOTES:
#    __init__(self [,...])          instance = MyClass(arg1, arg2)    called on instance creation
#    __setitem__(self, key, val)    self[key] = val                   assigning to an item using an index
#    __getitem__(self, key)         self[key]                         accessing an item using an index
#    __str__(self)                  str()                             produce human readable output 
#    The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
#    If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

ORIENTATIONS = {'f': 'front', 'r': 'right', 'b': 'back', 'l': 'left', 'u': 'up', 'd': 'down'}
OFFSETS = {'f': 0, 'r': 9, 'b': 18, 'l': 27, 'u': 36, 'd': 45}
JUST_NAMES = list(ORIENTATIONS.values())
JUST_ABBR = list(ORIENTATIONS.keys()) # not used but might come in handy

# blocks attached to the sides of each orientation
# !!!!!!! NUMBERING STARTS AT 0 !!!!!!! NOT LIKE ON SLIDES !!!!!!!
CONNECTED = {   'f': ((42, 43, 44), (9, 12, 15), (47, 46, 45), (35, 32, 29)),   'r': ((44, 41, 38), (18, 21, 24), (53, 50, 47), (8, 5, 2)),
                'b': ((38, 37, 36), (27, 30, 33), (51, 52, 53), (17, 14, 11)),  'l': ((36, 39, 42), (0, 3, 6), (45, 48, 51), (26, 23, 20)),
                'u': ((20, 19, 18), (11, 10, 9), (2, 1, 0), (29, 28, 27)),      'd': ((6, 7, 8), (15, 16, 17), (24, 25, 26), (33, 34, 35))}

# rotation orientations for looping
FRONT = {'offset': 0, 'F': 'F', 'f': 'f', 'R': 'R', 'r': 'r', 'B': 'B', 'b': 'b', 'L': 'L', 'l': 'l'}
RIGHT = {'offset': 9, 'F': 'R', 'f': 'r', 'R': 'B', 'r': 'b', 'B': 'L', 'b': 'l', 'L': 'F', 'l': 'f'}
BACK = {'offset': 18, 'F': 'B', 'f': 'b', 'R': 'L', 'r': 'l', 'B': 'F', 'b': 'f', 'L': 'R', 'l': 'r'}
LEFT = {'offset': 27, 'F': 'L', 'f': 'l', 'R': 'F', 'r': 'f', 'B': 'R', 'b': 'r', 'L': 'B', 'l': 'b'}

class Cube:
    
    # called on instance creation
    def __init__(self, cube_str):
        self.solution = []
        self.cube_build = {
            colors: [
                [cube_str[offset + 0], cube_str[offset + 1], cube_str[offset + 2]],
                [cube_str[offset + 3], cube_str[offset + 4], cube_str[offset + 5]],
                [cube_str[offset + 6], cube_str[offset + 7], cube_str[offset + 8]],
            ]
            for colors, offset in zip(ORIENTATIONS.values(), OFFSETS.values())
        }
    
    # assigning to an item using an index
    def __setitem__(self, key, val):
        self.cube_build[JUST_NAMES[key // 9]][key % 9 // 3][key % 3] = val
    
    # accessing an item using an index
    def __getitem__(self, key):
        return self.cube_build[JUST_NAMES[key // 9]][key % 9 // 3][key % 3]
    
    # produce human readable output
    def __str__(self):
        return ''.join(f'{i[0][0]}{i[0][1]}{i[0][2]}{i[1][0]}{i[1][1]}{i[1][2]}{i[2][0]}{i[2][1]}{i[2][2]}' for i in (self.cube_build[j] for j in ORIENTATIONS.values()))
    
    # rotate selection    
    def rotate(self, rotations):
        # upper case - clockwise, lower case - counterclockwise
        for rotation in rotations:
            direction = rotation.isupper()
            self.rotate_face(rotation, direction)
            self.rotate_connected(rotation, direction)
            self.solution += rotation
            
    # rotate selected face    
    def rotate_face(self, rotation, direction):
        offset = OFFSETS[rotation.lower()]
        for x in range(0, 1):
                for y in range(x, 2 - x):
                    z = self[offset + (x * 3 + y)]
                    # CLOCKWISE
                    if direction == True:
                        # move colors around
                        self[offset + (x * 3 + y)] = self[offset + ((2 - y) * 3 + x)]
                        self[offset + ((2 - y) * 3 + x)] = self[offset + ((2 - x) * 3 + (2 - y))]
                        self[offset + ((2 - x) * 3 + (2 - y))] = self[offset + (y * 3 + (2 - x))]
                        self[offset + (y * 3 + (2 - x))] = z
                    # COUNTER CLOCKWISE
                    else:
                        # move colors around
                        self[offset + (x * 3 + y)] = self[offset + (y * 3 + (2 - x))]
                        self[offset + (y * 3 + (2 - x))] = self[offset + ((2 - x) * 3 + (2 - y))]
                        self[offset + ((2 - x) * 3 + (2 - y))] = self[offset + ((2 - y) * 3 + x)]
                        self[offset + ((2 - y) * 3 + x)] = z
    
    # rotate blocks connected to selected face                
    def rotate_connected(self, rotation, direction):
        connected = zip(*CONNECTED[rotation.lower()])
        for a, b, c, d in connected:
            e = self[a]
            # CLOCKWISE
            if direction == True:
                # move colors around
                self[a] = self[d]
                self[d] = self[c]
                self[c] = self[b]
                self[b] = e
            # COUNTER CLOCKWISE
            else:
                # move colors around
                self[a] = self[b]
                self[b] = self[c]
                self[c] = self[d]
                self[d] = e
    
    # solve cube according to iteration
    def solveCube(self):
        front_face =    [self[0],  self[1],  self[2],  self[3],  self[4],  self[5],  self[6],  self[7],  self[8]]
        right_face =    [self[9],  self[10], self[11], self[12], self[13], self[14], self[15], self[16], self[17]]
        back_face =     [self[18], self[19], self[20], self[21], self[22], self[23], self[24], self[25], self[26]]
        left_face =     [self[27], self[28], self[29], self[30], self[31], self[32], self[33], self[34], self[35]]
        up_face =       [self[36], self[37], self[38], self[39], self[40], self[41], self[42], self[43], self[44]]
        down_face =     [self[45], self[46], self[47], self[48], self[49], self[50], self[51], self[52], self[53]]
        
        # if solved
        if (all(color == self[4] for color in front_face) and all(color == self[13] for color in right_face) and
            all(color == self[22] for color in back_face) and all(color == self[31] for color in left_face) and
            all(color == self[40] for color in up_face) and all(color == self[49] for color in down_face)):
            
            return
        
        else:
            
            # if down face already solved
            if all(color == self[49] for color in [self[45], self[46], self[47], self[48], self[50], self[51], self[52], self[53]]):
                return
            
            # if bottom cross already solved
            elif all(color == self[49] for color in [self[46], self[48], self[50], self[52]]):
                self.makeDownFace()
            
            # if up daisy already solved
            elif all(color == self[49] for color in [self[37], self[39], self[41], self[43]]):
                self.makeBottomCross()
                self.makeDownFace()
                
            # if scrambled
            else:
                self.makeDaisy()
                self.makeBottomCross()
                self.makeDownFace()
                
    def makeDownFace(self):
        # form down face from other formations
        while all(color == self[49] for color in [self[45], self[46], self[47], self[48], self[50], self[51], self[52], self[53]]) is False:
            bottom_corners = [self[6], self[8], self[15], self[17], self[24], self[26], self[33], self[35]]
            if any(color == self[49] for color in bottom_corners):
                self.bottomCornerToUpFace()
                
            up_face_corners = [self[36], self[38], self[42], self[44]]
            if any(color == self[49] for color in up_face_corners):
                self.upFaceToTopCorner()
                
            top_corners = [self[0], self[2], self[9], self[11], self[18], self[20], self[27], self[29]]
            if any(color == self[49] for color in top_corners):
                self.topCornerToDownFace()
    
    def topCornerToDownFace(self):
        # move top corners to down face
        top_corners = [self[0], self[2], self[9], self[11], self[18], self[20], self[27], self[29]]
        if any(color == self[49] for color in top_corners):
            while True:
                if self[0] == self[49] or self[2] == self[49]:
                    offset = 0
                    F, f, R, r, B, b, L, l, U, u, D, d = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'
                # right orientation
                elif self[9] == self[49] or self[11] == self[49]:
                    offset = 9
                    F, f, R, r, B, b, L, l, U, u, D, d = 'R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u', 'D', 'd'
                # back orientation
                elif self[18] == self[49] or self[20] == self[49]:
                    offset = 18
                    F, f, R, r, B, b, L, l, U, u, D, d = 'B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u', 'D', 'd'
                # left orientation
                elif self[27] == self[49] or self[29] == self[49]:
                    offset = 27
                    F, f, R, r, B, b, L, l, U, u, D, d = 'L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u', 'D', 'd'
                        
                if self[offset + 2] == self[49]:
                    if self[(offset + 9) % 36] != self[(offset + 13) % 36]:
                        while True:
                            self.rotate('U')
                            if self[(offset + 9) % 36] == self[(offset + 13) % 36]:
                                break
                        self.rotate(f + u + F)
                    else:
                        self.rotate(f + u + F)
                        
                if self[offset + 0] == self[49]:
                    if self[(offset + 29) % 36] != self[(offset + 31) % 36]:
                        while True:
                            self.rotate('U')
                            if self[(offset + 29) % 36] == self[(offset + 31) % 36]:
                                break
                        self.rotate(F + U + f)
                    else:
                        self.rotate(F + U + f)
                    
                top_corners = [self[0], self[2], self[9], self[11], self[18], self[20], self[27], self[29]]        
                if any(color == self[49] for color in top_corners) is False:
                    break
            
    
    def upFaceToTopCorner(self):
        # move up face corners to top corners
        up_face_corners = [self[36], self[38], self[42], self[44]]
        while any(color == self[49] for color in up_face_corners):
            if self[42] == self[49]:
                self.rotate('luuL')
            if self[44] == self[49]:
                self.rotate('RUUr')
            if self[36] == self[49]:
                self.rotate('LUUl')
            if self[38] == self[49]:
                self.rotate('ruuR')
            
            bottom_corners = [self[6], self[8], self[15], self[17], self[24], self[26], self[33], self[35]]    
            if any(color == self[49] for color in bottom_corners):
                self.bottomCornerToUpFace()
            
            up_face_corners = [self[36], self[38], self[42], self[44]]
            if any(color == self[49] for color in up_face_corners) is False:
                break
            
    def bottomCornerToUpFace(self):
        # move bottom corners to up face
        bottom_corners = [self[6], self[8], self[15], self[17], self[24], self[26], self[33], self[35]]
        while any(color == self[49] for color in bottom_corners):
            # front orientation
            if self[6] == self[49] or self[8] == self[49]:
                offset = 0
                F, f, R, r, B, b, L, l, U, u, D, d = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'
            # right orientation
            elif self[15] == self[49] or self[17] == self[49]:
                offset = 9
                F, f, R, r, B, b, L, l, U, u, D, d = 'R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u', 'D', 'd'
            # back orientation
            elif self[24] == self[49] or self[26] == self[49]:
                offset = 18
                F, f, R, r, B, b, L, l, U, u, D, d = 'B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u', 'D', 'd'
            # left orientation
            elif self[33] == self[49] or self[35] == self[49]:
                offset = 27
                F, f, R, r, B, b, L, l, U, u, D, d = 'L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u', 'D', 'd'
            
            if self[offset + 6] == self[49]:
                self.rotate(l + u + L)
            if self[offset + 8] == self[49]:
                self.rotate(R + U + r)
                
            bottom_corners = [self[6], self[8], self[15], self[17], self[24], self[26], self[33], self[35]]    
            if any(color == self[49] for color in bottom_corners) is False:
                break
    
    def makeBottomCross(self):
        bottom_cross = [self[46], self[50], self[52], self[48]]
        # if bottom cross not solved
        if bottom_cross != [self[49], self[49], self[49], self[49]]:
            # form cross front
            if self[1] != self[4]:
                while True:
                    self.rotate('U')
                    if self[1] == self[4]:
                        break
                self.rotate('FF')
            else:
                self.rotate('FF')
            # form cross right
            if self[10] != self[13]:
                while True:
                    self.rotate('U')
                    if self[10] == self[13]:
                        break
                self.rotate('RR')
            else:
                self.rotate('RR')
            # form cross back
            if self[19] != self[22]:
                while True:
                    self.rotate('U')
                    if self[19] == self[22]:
                        break
                self.rotate('BB')
            else:
                self.rotate('BB')
            # form cross left
            if self[28] != self[31]:
                while True:
                    self.rotate('U')
                    if self[28] == self[31]:
                        break
                self.rotate('LL')
            else:
                self.rotate('LL')

    def makeDaisy(self):
        daisy = [self[37], self[39], self[41], self[43]]
        # if daisy not solved
        if any(color != self[49] for color in daisy):
            # while daisy not solved
            while True:
                # front orientation
                if self[43] != self[49]:
                    offset = FRONT.get('offset')
                    F, f, R, l, U, u, D, d = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'
                # right orientation
                elif self[41] != self[49]:
                    offset = RIGHT.get('offset')
                    F, f, R, r, B, b, L, l, U, u, D, d = 'R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u', 'D', 'd'
                # back orientation
                elif self[37] != self[49]:
                    offset = BACK.get('offset')
                    F, f, R, r, B, b, L, l, U, u, D, d = 'B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u', 'D', 'd'
                # left orientation
                elif self[39] != self[49]:
                    offset = LEFT.get('offset')
                    F, f, R, r, B, b, L, l, U, u, D, d = 'L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u', 'D', 'd'
                # face up middle
                if self[(offset + 1) % 36] == self[49]:
                    self.rotate(f + 'U' + l + 'u')
                # face left middle
                elif self[(offset + 3) % 36] == self[49]:
                    self.rotate('U' + l + 'u')
                # face right middle
                elif self[(offset + 5) % 36] == self[49]:
                    self.rotate(u + R + U)
                # face down middle
                elif self[(offset + 7) % 36] == self[49]:
                    self.rotate(f + u + R + U)
                # face right adjacent
                elif self[(offset + 12) % 36] == self[49]:
                    self.rotate(f)
                # face left adjacent
                elif self[(offset + 32) % 36] == self[49]:
                    self.rotate(F)
                # front down adjacent
                elif offset == 0:
                    if self[46] == self[49]:
                        self.rotate(F + F)
                    if self[50] == self[49]:
                        self.rotate(d + F + F)
                    if self[52] == self[49]:
                        self.rotate(d + d + F + F)
                    if self[48] == self[49]:
                        self.rotate(D + F + F)
                # right down adjacent
                elif offset == 9:
                    if self[46] == self[49]:
                        self.rotate(D + F + F)
                    if self[50] == self[49]:
                        self.rotate(F + F)
                    if self[52] == self[49]:
                        self.rotate(d + F + F)
                    if self[48] == self[49]:
                        self.rotate(d + d + F + F)
                # back down adjacent
                elif offset == 18:
                    if self[46] == self[49]:
                        self.rotate(d + d + F + F)
                    if self[50] == self[49]:
                        self.rotate(D + F + F)
                    if self[52] == self[49]:
                        self.rotate(F + F)
                    if self[48] == self[49]:
                        self.rotate(d + F + F)
                # left down adjacent
                elif offset == 27:
                    if self[46] == self[49]:
                        self.rotate(d + F + F)
                    if self[50] == self[49]:
                        self.rotate(d + d + F + F)
                    if self[52] == self[49]:
                        self.rotate(D + F + F)
                    if self[48] == self[49]:
                        self.rotate(F + F)
                # break condition
                daisy = [self[37], self[39], self[41], self[43]]
                if daisy == [self[49], self[49], self[49], self[49]]:
                    break
