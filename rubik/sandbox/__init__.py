
# rrrrrrrrrgggggggggooooooooobbbbbbbbbyyyyyyyyywwwwwwwww    solved
# ybooroyywyybbgwogoywroorwrwbbrybyrgrwgorygbwggbbowrgwg    scrambled
# ybrgrooywwrybgrogbgobbooorgwgrgbyrygrwowywbwgwbbowryyy    up daisy
# gyrgrbrrygrbrggrgbwgyooooowgyobbyobworroyywbygwbwwwbwy    down cross
# googrrrrrbrybgbgggbgoyoyoooygrobobbbgrryyyybywwwwwwwww    down face

cube = 'ybooroyywyybbgwogoywroorwrwbbrybyrgrwgorygbwggbbowrgwg'

front_face =    [cube[0],  cube[1],  cube[2],  cube[3],  cube[4],  cube[5],  cube[6],  cube[7],  cube[8]]
right_face =    [cube[9],  cube[10], cube[11], cube[12], cube[13], cube[14], cube[15], cube[16], cube[17]]
back_face =     [cube[18], cube[19], cube[20], cube[21], cube[22], cube[23], cube[24], cube[25], cube[26]]
left_face =     [cube[27], cube[28], cube[29], cube[30], cube[31], cube[32], cube[33], cube[34], cube[35]]
up_face =       [cube[36], cube[37], cube[38], cube[39], cube[40], cube[41], cube[42], cube[43], cube[44]]
down_face =     [cube[45], cube[46], cube[47], cube[48], cube[49], cube[50], cube[51], cube[52], cube[53]]

print('F:', ' '.join(front_face))
print('R', right_face)
print('B', back_face)
print('L', left_face)
print('U', up_face)
print('D', down_face)

# if bottom layer solved
if all(color == cube[49] for color in [cube[45], cube[46], cube[47], cube[48], cube[50], cube[51], cube[52], cube[53]]):
    print('solved')
    
# if bottom cross solved
elif all(color == cube[49] for color in [cube[46], cube[48], cube[50], cube[52]]):
    print('solve bottom layer')
    print('solved')

# if up daisy solved
elif all(color == cube[49] for color in [cube[37], cube[39], cube[41], cube[43]]):
    print('solve bottom cross')
    print('solve bottom layer')
    print('solved')
    
else:
    print('solve up daisy')
    print('solve bottom cross')
    print('solve bottom layer')
    print('solved')