from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_01_Ok_SolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'ok')

    def test_check_02_Error_CubeMissing(self):
        parm = {'op':'check',
                'cube': None}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: cube missing')
        
    def test_check_03_Error_NotAString(self):
        parm = {'op':'check',
                'cube': 123456789}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: not a string')
        
    def test_check_04_Error_InvalidCharacters(self):
        parm = {'op':'check',
                'cube': '!#%&?'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: invalid characters')

    def test_check_05_Error_InvalidSize(self):
        parm = {'op':'check',
                'cube':'0123456789'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: invalid size')
        
    def test_check_06_Error_NumberOfColors(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrggggggggooooooooyyyyyyyywwwwwwwwzzzzzz'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: number of colors')
        
    def test_check_07_Error_InvalidCenters(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrgrrrrggggoggggooooyooooyyyywyyyywwwwbwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: invalid centers')
        
    def test_check_08_Error_AmountOfEachColor(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbbbbbrbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: amount of each color')
        