import rubik.cube as rubik

def _solve(parms):
    result = {}
    encodedCube = parms.get('cube',None)       #get "cube" parameter if present
    result['solution'] = 'FfRrBbLlUuDd'        #example rotations
    result['status'] = 'ok'                     
    return result

# needs to:
#    validate parms
#    load parms['cube'] into cube model
#    rotate cube in desired direction
#    serialize cube model in string
#    return string + status of 'ok'