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
        print("CT 01 PASSED - Ok_SolvedCube")

    def test_check_02_Error_CubeMissing(self):
        parm = {'op':'check',
                'cube': None}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: cube missing')
        print("CT 02 PASSED - Error_CubeMissing")
        
    def test_check_03_Error_NotAString(self):
        parm = {'op':'check',
                'cube': 123456789}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: not a string')
        print("CT 03 PASSED - Error_NotAString")
        
    def test_check_04_Error_InvalidCharacters(self):
        parm = {'op':'check',
                'cube': '!#%&?'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: invalid characters')
        print("CT 04 PASSED - Error_InvalidCharacters")

    def test_check_05_Error_InvalidSize(self):
        parm = {'op':'check',
                'cube':'0123456789'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: invalid size')
        print("CT 05 PASSED - Error_InvalidSize")
        
    def test_check_06_Error_NumberOfColors(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrggggggggooooooooyyyyyyyywwwwwwwwzzzzzz'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: number of colors')
        print("CT 06 PASSED - Error_NumberOfColors")
        
    def test_check_07_Error_InvalidCenters(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrgrrrrggggoggggooooyooooyyyywyyyywwwwbwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: invalid centers')
        print("CT 07 PASSED - Error_InvalidCenters")
        
    def test_check_08_Error_AmountOfEachColor(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbbbbbrbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertEqual(status, 'error: amount of each color')
        print("CT 08 PASSED - Error_AmountOfEachColor")
        