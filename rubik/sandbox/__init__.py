#right_trigger = cube.rotate('RUr')
#left_trigger = cube.rotate('luL')
#bottom_layer = [cube[45], cube[46], cube[47], cube[48], cube[50], cube[51], cube[52], cube[53]]
# if bottom layer not solved
#if bottom_layer != [cube[49], cube[49], cube[49], cube[49], cube[49], cube[49], cube[49], cube[49]]:
#   cube.makeBottomCross()

#cube = '2255aHaaaH2a5555555G2GH2HHHGGGH2a222HaGHGaaGGxxxxxxxxx'    shouldSolveBottomOnSolvedCube
#cube = '2255aHaaaH2a5555555G2GH2HHHGGGH2a222HaGHGaaGGxxxxxxxxx'    shouldSolveBottomOnSolvedBottom
#cube = 'GRQQRRpRpGGQGpQQpwwpwpwRtwptwRQGwtGQGwGGQQtpRRtwtttRtp'    shouldSolveBottomOnDownFaceDaisy
#cube = 'oioiOpiMciMMOMMpiMcocOioOpcMoOOppiOoOiipoopMpMcOcccpco'    shouldSolveBottomWithMisalignedDaisy

cube = 'oioiOpiMciMMOMMpiMcocOioOpcMoOOppiOoOiipoopMpMcOcccpco'

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