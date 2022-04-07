import unittest
import requests 
import json
import datetime
import os
import sys
import re
import inspect
import string
import random
import logging 


class SmartTestCase(unittest.TestCase):

    def run(self, result):
        # Store the result on the class so tearDown can behave appropriately
        self.result = result.result if hasattr(result, 'result') else result
        if PY >= (3, 4, 0):
            self._feedErrorsToResultEarly = self._feedErrorsToResult
            self._feedErrorsToResult = lambda *args, **kwargs: None  # no-op
        super(SmartTestCase, self).run(result)

    @property
    def errored(self):
        if (3, 0, 0) <= PY < (3, 4, 0):
            return bool(self._outcomeForDoCleanups.errors)
        return self.id() in [case.id() for case, _ in self.result.errors]

    @property
    def failed(self):
        if (3, 0, 0) <= PY < (3, 4, 0):
            return bool(self._outcomeForDoCleanups.failures)
        return self.id() in [case.id() for case, _ in self.result.failures]

    @property
    def passed(self):
        return not (self.errored or self.failed)

    def tearDown(self):
        if PY >= (3, 4, 0):
            self._feedErrorsToResultEarly(self.result, self._outcome.errors)


class A3AcceptanceTest(SmartTestCase):
    happyCount = 0
    happyFailed = 0
    sadCount = 0
    sadFailed = 0
    extraCreditCount = 0
    extraCreditFailed = 0

    @classmethod
    def setUpClass(cls):   
        cls.instructorURL = "https://rubik-cube.mybluemix.net/rubik"
        cls.testURL = os.environ["url"] + "/rubik"
        cls.userName = os.environ["name"]
        
        cls.cubeKey = 'cube'
        cls.statusKey = 'status'
        cls.statusOk = 'ok' 
        cls.statusError = 'error:'                                   
      
    @classmethod  
    def tearDownClass(cls):
        log.info("----> Assignment3")  
        log.info("      " + os.environ["name"])   
        log.info(f'\tA3: happy path test count --> {A3AcceptanceTest.happyCount}')
        log.info(f'\tA3: happy path tests not passed --> {A3AcceptanceTest.happyFailed}')
        log.info(f'\tA3: sad path test count --> {A3AcceptanceTest.sadCount}')
        log.info(f'\tA3: sad path tests not passed --> {A3AcceptanceTest.sadFailed}')
        log.info(f'\tA3: extra credit test count --> {A3AcceptanceTest.extraCreditCount}')
        log.info(f'\tA3: extra credit tests not passed --> {A3AcceptanceTest.extraCreditFailed}')
        log.info("@@@@" + os.environ["name"] + "@@@@" )
 
    def setUp(self):
        super(A3AcceptanceTest, self).setUp()
        log.info('---------------------------------------')
        log.info('RUNNING {} '.format(self.id()))
            
    def tearDown(self):
        def splitCount(caseNumber, count1, count2, count3):
            if(caseNumber < 900):
                count1 += 1
            elif(caseNumber < 990):
                count2 += 1
            else:
                count3 += 1
            return (count1, count2, count3)
                
        super(A3AcceptanceTest, self).tearDown()
        try:
            testNumber = int(re.search(r'(?<=_)\d\d\d+', self.id()).group(0))
            A3AcceptanceTest.happyCount, A3AcceptanceTest.sadCount, A3AcceptanceTest.extraCreditCount = \
                splitCount(testNumber, A3AcceptanceTest.happyCount, A3AcceptanceTest.sadCount, A3AcceptanceTest.extraCreditCount)
            if (self.errored | self.failed):
                A3AcceptanceTest.happyFailed, A3AcceptanceTest.sadFailed, A3AcceptanceTest.extraCreditFailed = \
                    splitCount(testNumber, A3AcceptanceTest.happyFailed, A3AcceptanceTest.sadFailed, A3AcceptanceTest.extraCreditFailed)                
        except:
            log.info('test number invalid ... ignored')
        if self.errored:
            log.info('\tERRORED -----')
        elif self.failed:
            log.info('\tFAILED -----')
        else:
            log.info('\tPASSED -----')
            
# microservice helper methods
    def microservice(self, theURL):
        '''Issue HTTP/HTTPS request and capture the JSON result'''
        try:
            log.debug("HTTP request-->" + theURL)
            theResponse = requests.get(theURL)
            theBody = theResponse.text
            theResult = {'statusCode': theResponse.status_code}
            log.debug("HTTP response-->" + theBody)
        except Exception as e:
            theResult['diagnostic1'] = str(e)
            theResult['statusCode'] = 999
            log.error(theResult)
            return theResult
             
        '''Convert JSON string to dictionary'''
        try:
            theJsonBody = theBody.replace('"', " ")
            theJsonBody = theJsonBody.replace("'", "\"")
            theDictionaryBody = json.loads(theJsonBody)
            for element in theDictionaryBody:
                if(isinstance(theDictionaryBody[element], str)):
                    theResult[str(element)] = str(theDictionaryBody[element])
                else:
                    theResult[str(element)] = theDictionaryBody[element]
        except Exception as e:
            theResult['diagnostic2'] = str(e)
            log.error("unable to parse JSON: '" + theBody+"'")

        return theResult 
     
# ------------------------------------------ 

# rubik-specific helper methods

    def invokeMicroservice(self, inputParmDict, theUrl):
        parmString = self.constructParms(inputParmDict)
        theURL = theUrl + '?' + '&'.join(parmString)
        actualResult = self.microservice(theURL)
        self.assertEqual(200, actualResult['statusCode'], 
                         f'Microservice not accessible at {theURL} [major]')
        return actualResult

    def constructParms(self, parmDict):
        parmString = []
        for key in parmDict:
            parmString.append(key + "=" + parmDict[key])    
        return parmString

    def buildNominalCube(self):
        defaultCube = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputParmDict = {
                            'op': 'solve',
                            'cube': self.generateNominalCube()
                         }
        actualResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        scrambledCube = actualResult.get('cube', defaultCube)     
        return scrambledCube

    def generateNominalCube(self):
        ELEMENTS_PER_SIDE = 9
        legalCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        randomColors = (random.sample(legalCharacters, k=6))
        encodedCube = ""
        for color in randomColors:
            encodedCube += color * ELEMENTS_PER_SIDE
        return encodedCube
    
    def scrambleCube(self, encodedCube):
        inputParmDict = {
                            'op': 'solve',
                            'cube': encodedCube,
                         }        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL) 
        scrambledCube = expectedResult.get('cube', 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy') 
        return scrambledCube
    
    def generateMultipleRotations(self):
        CANDIDATE_ROTATIONS = ['F', 'f',
                               'R', 'r',
                               'B', 'b',
                               'L', 'l',
                               'U', 'u',
                               'D', 'd']
        randomRotations = random.choices(CANDIDATE_ROTATIONS, k=25)
        randomRotationString = "".join(randomRotations)
        return randomRotationString
       
    def specs(self): 
#-------------------------------------------------------------------------------
# Analysis
#    rubik?op=solve&rotate=R&cube=gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy
#
#    inputs:   can occur in any order
#        op            value of "solve"; mandatory; arrives validated
#        rotate        string consisting of [FfRrBbLlUuDd] or empty string ; 
#                        optional, defaults to "F" if missing or ""; 
#                        arrives unvalidated
#        cube          string; 54 characters, [azAZ09], 
#                        9 occurrences of 6 characters, 
#                        middle face is each of 6 characters;
#                        mandatory; 
#                        arrives unvalidated
#
#    outputs:
#        side-effects:  no state change; no external effects
#        returns:  JSON string consisting of 
#            nominal (in any order)
#                {
#                    'cube':        54 character serialization of rotated cube
#                    'status':      'ok'
#                }
#            abnormal:
#                {
#                    'status':      'error: xxx' where xxx is dev-selected message, len>0
#                }
#
#    confidence level:  boundary value analysis
#
#    happy path:
#        test 005:  nominal cube, F rotation
#        test 010:  nominal cube, f rotation
#        test 015:  nominal cube, R rotation
#        test 020:  nominal cube, r rotation
#        test 025:  nominal cube, B rotation
#        test 030:  nominal cube, b rotation
#        test 035:  nominal cube, L rotation
#        test 040:  nominal cube, l rotation
#        test 045:  nominal cube, U rotation
#        test 050:  nominal cube, u rotation
#        test 055:  nominal cube, D rotation
#        test 060:  nominal cube, d rotation
#        test 065:  nominal cube, multirotations
#        test 070:  nominal cube, missing rotation
#        test 075:  nominal cube, empty rotation
#        test 080:  inverted parm order
#        test 085:  extraneous keys
#
#    sad path:
#        test 905:  missing cube
#        test 910:  short cube
#        test 915:  long cube
#        test 920:  cube with illegal characters, valid otherwise
#        test 925:  cube with != 9 occurrences of at least one of 6 unique characters
#        test 930:  cube with more than 6 unique characters
#        test 935:  cube non-unique middle face#        test 015:  nominal cube, R rotation
#        test 940:  nominal cube, invalid single rotation
#        test 945:  nominal cube, invalid embedded multiple rotation
#
        pass
    
    def testA3_solve_005_shouldRotateFOnNominalCube(self):
#        test 005:  nominal cube, F rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'F',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA3_solve_010_shouldRotatefOnNominalCube(self):
#        test 010:  nominal cube, f rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'f',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA3_solve_015_shouldRotateROnNominalCube(self):
#        test 015:  nominal cube, R rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'R',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA3_solve_020_shouldRotaterOnNominalCube(self):
#        test 020:  nominal cube, r rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'r',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_025_shouldRotateBOnNominalCube(self):
#        test 025:  nominal cube, B rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'B',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_030_shouldRotatebOnNominalCube(self):
#        test 030:  nominal cube, b rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'b',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_035_shouldRotateLOnNominalCube(self):
#        test 035:  nominal cube, L rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'L',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_040_shouldRotatelOnNominalCube(self):
#        test 040:  nominal cube, l rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'l',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_045_shouldRotateUOnNominalCube(self):
#        test 045:  nominal cube, U rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'U',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_050_shouldRotateuOnNominalCube(self):
#        test 050:  nominal cube, u rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'u',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_055_shouldRotateDOnNominalCube(self):
#        test 055:  nominal cube, D rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'D',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_060_shouldRotatedOnNominalCube(self):
#        test 010:  nominal cube, d rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'd',
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_065_shouldRotateMultipleOnNominalCube(self):
#        test 065:  nominal cube, multirotations
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        multipleRotations = self.generateMultipleRotations()
        inputParmDict = {
                            'op': 'solve',
                            'rotate': multipleRotations,
                            'cube': scrambledCube,
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_070_shouldRotateFOnNominalCubeMissingRotation(self):
#        test 070:  nominal cube, missing rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'cube': scrambledCube,
                         }
        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        inputParmDict['rotate'] = 'F'
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    
# ------------------------------------------

    def testA3_solve_075_shouldRotateFOnNominalCubeEmptyRotation(self):
#        test 010:  nominal cube, f rotation
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': '',
                            'cube': scrambledCube,
                         }
        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        inputParmDict['rotate'] = 'F'
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)
    

# ------------------------------------------

    def testA3_solve_080_shouldRotateOnNominalCubeNominalRotateUnordered(self):
#        test 080:  nominal cube, nominal rotation, reversed order
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'cube': scrambledCube,
                            'op': 'solve',
                            'rotate': 'F',
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA3_solve_085_shouldIgnoreExtraneousParms(self):
#        test 085:  nominal cube, nominal rotation, extra keys
#                    result:  rotation verified by instructor microservice
        encodedCube = self.generateNominalCube()
        scrambledCube = self.scrambleCube(encodedCube)
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'r',
                            'cube': scrambledCube,
                            'extraneousKey': 'this should be ignored'
                         }
        
        expectedResult = self.invokeMicroservice(inputParmDict, self.instructorURL)        
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)
        
        self.assertDictEqual(expectedResult, actualResult,
                             'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA3_solve_905_shouldErrOnMissingCube(self):
#        test 905:  missing cube, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'rotate': 'F'
                        }
        
        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)

# ------------------------------------------

    def testA3_solve_910_shouldErrOnShortCube(self):
#        test 910:  <54 character cube, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbbrrrrrrrrrggggggggg',
                            'rotate': 'F'
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA3_solve_915_shouldErrOnLongCube(self):
#        test 915:  >54 character cube, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww',
                            'rotate': 'F'
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA3_solve_920_shouldErrOnCubeWithIllegalCharcters(self):
#        test 920:  cube with characters other than [azAZ09], nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbb         gggggggggoooooooooyyyyyyyyywwwwwwwww',
                            'rotate': 'F'
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA3_solve_925_shouldErrOnCubeWithIncorrectColorOccurrences(self):
#        test 910:  cube having other than 9 of each color, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                            'rotate': 'F'
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA3_solve_930_shouldErrOnCubeWithOtherThan6UniqueCharacters(self):
#        test 930:  cube having other than 6 of each color, nominal rotatio
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwe',
                            'rotate': 'F'
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA3_solve_935_shouldErrOnCubeWithNonUniqueMiddles(self):
#        test 935:  cube with duplicate middle colors, nominal rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': 'bbbbbbbbrrrrrbrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww',
                            'rotate': 'F'
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA3_solve_940_shouldErrOnInvalidSingleRotation(self):
#        test 935:  nominal cube, invalid single rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': self.generateNominalCube(),
                            'rotate': 'z'
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        
# ------------------------------------------

    def testA3_solve_945_shouldErrOnEmbeddedInvalidRotation(self):
#        test 935:  nominal cube, invalid embedded multiple rotation
#                    result:  'status': 'error: xxx', where xxx is dev-dependent
        inputParmDict = {
                            'op': 'solve',
                            'cube': self.generateNominalCube(),
                            'rotate': 'Ff Bb'
                        }

        expectedResult = 'error: '
        actualResult = self.invokeMicroservice(inputParmDict, self.testURL)        
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
        


# ------------------------------------------

if __name__ == "__main__":
    try:
        print(" ")
        print("@A3   " + os.environ["name"])      
        # print("      " + os.environ["url"])
        print("      " + str(datetime.datetime.now()))
        print("+------------------------------------------------------------------")    
    except:
        print("@A3  -- identifying information missing")
        sys.exit()
        
    formatter = logging.Formatter(fmt='%(levelname)-8s %(name)s: %(message)s')
    # log_file = os.path.splitext(os.path.abspath(__file__))[0] + '.log'
    log_file = os.environ["name"] + ".log"
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)
    logging.root.setLevel(logging.DEBUG)
    log = logging.getLogger(__name__)
    PY = tuple(sys.version_info)[:3]
    log.info("+------------------------------------------------------------------") 
    log.info("@A3  " + os.environ["name"])  
    # log.info("      " + os.environ["url"])
    log.info("      " + str(datetime.datetime.now()))
    
    unittest.main()
