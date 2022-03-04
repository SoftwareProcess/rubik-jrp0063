
# NOTES:
#    __init__(self [,...])          instance = MyClass(arg1, arg2)    called on instance creation
#    __setitem__(self, key, val)    self[key] = val                   assigning to an item using an index
#    __getitem__(self, key)         self[key]                         accessing an item using an index
#    __str__(self)                  str()                             produce human readable output 

# JONATHON FIX THIS IT'S UGLY
ORIENTATIONS = {'f': 'front', 'r': 'right', 'b': 'back', 'l': 'left', 'u': 'up', 'd': 'down'}
OFFSETS = {'f': 0, 'r': 9, 'b': 18, 'l': 27, 'u': 36, 'd': 45}
JUST_ABBR = list(ORIENTATIONS.keys())
JUST_NAMES = list(ORIENTATIONS.values())

ADJACENTS = {
    'f': ((42, 43, 44), (9, 12, 15), (47, 46, 45), (35, 32, 29)),
    'r': ((44, 41, 38), (18, 21, 24), (53, 50, 47), (8, 5, 2)),
    'b': ((38, 37, 36), (27, 30, 33), (51, 52, 53), (17, 14, 11)),
    'l': ((36, 39, 42), (0, 3, 6), (45, 48, 51), (26, 23, 20)),
    'u': ((20, 19, 18), (11, 10, 9), (2, 1, 0), (29, 28, 27)),
    'd': ((6, 7, 8), (15, 16, 17), (24, 25, 26), (33, 34, 35)),
}

class Cube:
    def __init__(self, cube_str):
        
        self.cube_build = {
            name: [
                [cube_str[offset + 0], cube_str[offset + 1], cube_str[offset + 2]],
                [cube_str[offset + 3], cube_str[offset + 4], cube_str[offset + 5]],
                [cube_str[offset + 6], cube_str[offset + 7], cube_str[offset + 8]],
            ]
            for name, offset in zip(ORIENTATIONS.values(), OFFSETS.values())
        }
            
    def __setitem__(self, key, val):
        self.cube_build[JUST_NAMES[key // 9]][key % 9 // 3][key % 3] = val
        
    def __getitem__(self, key):
        return self.cube_build[JUST_NAMES[key // 9]][key % 9 // 3][key % 3]
        
    def __str__(self):
        result = ''.join(f'{i[0][0]}{i[0][1]}{i[0][2]}{i[1][0]}{i[1][1]}{i[1][2]}{i[2][0]}{i[2][1]}{i[2][2]}' for i in (self.cube_build[j] for j in ORIENTATIONS.values()))
        return result
        
    def rotate(self, rotation):
        # upper case - clockwise, lower case - counterclockwise
        direction = rotation.isupper()
        self.rotate_face(rotation, direction)
        self.rotate_adjacents(rotation, direction)
        
    def rotate_face(self, rotation, direction):
        offset = OFFSETS[rotation.lower()]
        for x in range(0, 1):
                for y in range(x, 2 - x):
                    temp = self[offset + (x * 3 + y)]
                    # CLOCKWISE
                    if direction == True:
                        self[offset + (x * 3 + y)] = self[offset + ((2 - y) * 3 + x)]
                        self[offset + ((2 - y) * 3 + x)] = self[offset + ((2 - x) * 3 + (2 - y))]
                        self[offset + ((2 - x) * 3 + (2 - y))] = self[offset + (y * 3 + (2 - x))]
                        self[offset + (y * 3 + (2 - x))] = temp
                    # COUNTER CLOCKWISE
                    else:
                        self[offset + (x * 3 + y)] = self[offset + (y * 3 + (2 - x))]
                        self[offset + (y * 3 + (2 - x))] = self[offset + ((2 - x) * 3 + (2 - y))]
                        self[offset + ((2 - x) * 3 + (2 - y))] = self[offset + ((2 - y) * 3 + x)]
                        self[offset + ((2 - y) * 3 + x)] = temp
                    
    def rotate_adjacents(self, rotation, direction):
            for a, b, c, d in zip(*ADJACENTS[rotation.lower()]):
                temp = self[a]
                # CLOCKWISE
                if direction == True:
                    self[a] = self[d]
                    self[d] = self[c]
                    self[c] = self[b]
                    self[b] = temp
                # COUNTER CLOCKWISE
                else:
                    self[a] = self[b]
                    self[b] = self[c]
                    self[c] = self[d]
                    self[d] = temp
        