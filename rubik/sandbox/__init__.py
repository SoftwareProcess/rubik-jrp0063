right_trigger = self.rotate('RUr')
left_trigger = self.rotate('luL')
bottom_layer = [self[45], self[46], self[47], self[48], self[50], self[51], self[52], self[53]]

# if bottom layer not solved
if bottom_layer != [self[49], self[49], self[49], self[49], self[49], self[49], self[49], self[49]]:
    self.makeBottomCross()