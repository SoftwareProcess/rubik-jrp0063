import rubik.cube as rubik
import rubik.check as check

def _solve(parms):
    result = {}
    if (result := check(parms)).get('status') != 'ok':
        return result