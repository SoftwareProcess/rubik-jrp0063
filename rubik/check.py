import rubik.cube as rubik

def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)       
    if(encodedCube == None):
        result['status'] = 'error: xxx'
    else:
        result['status'] = 'ok'
    return result