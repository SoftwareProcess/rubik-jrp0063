import unittest
import os
import datetime
import sys
import logging
import re
import inspect
import rubik.check as check

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


class A2AcceptanceTest(SmartTestCase):
    happyCount = 0
    happyFailed = 0
    sadCount = 0
    sadFailed = 0
    extraCreditCount = 0
    extraCreditFailed = 0

    @classmethod
    def setUpClass(cls):      
        cls.userID = os.environ["id"]
        cls.userName = os.environ["name"]
        
        cls.cubeKey = 'cube'
        cls.statusKey = 'status'
        cls.statusOk = 'ok' 
        cls.statusError = 'error:'                                   
      
    @classmethod  
    def tearDownClass(cls):
        log.info("----> Assignment2")  
        log.info("      " + os.environ["name"])   
        log.info(f'\tA2: happy path test count --> {A2AcceptanceTest.happyCount}')
        log.info(f'\tA2: happy path tests not passed --> {A2AcceptanceTest.happyFailed}')
        log.info(f'\tA2: sad path test count --> {A2AcceptanceTest.sadCount}')
        log.info(f'\tA2: sad path tests not passed --> {A2AcceptanceTest.sadFailed}')
        log.info(f'\tA2: extra credit test count --> {A2AcceptanceTest.extraCreditCount}')
        log.info(f'\tA2: extra credit tests not passed --> {A2AcceptanceTest.extraCreditFailed}')
        log.info("@@@@" + os.environ["name"] + "@@@@" )
 
    def setUp(self):
        super(A2AcceptanceTest, self).setUp()
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
                
        super(A2AcceptanceTest, self).tearDown()
        try:
            testNumber = int(re.search(r'(?<=_)\d\d\d+', self.id()).group(0))
            A2AcceptanceTest.happyCount, A2AcceptanceTest.sadCount, A2AcceptanceTest.extraCreditCount = \
                splitCount(testNumber, A2AcceptanceTest.happyCount, A2AcceptanceTest.sadCount, A2AcceptanceTest.extraCreditCount)
            if (self.errored | self.failed):
                A2AcceptanceTest.happyFailed, A2AcceptanceTest.sadFailed, A2AcceptanceTest.extraCreditFailed = \
                    splitCount(testNumber, A2AcceptanceTest.happyFailed, A2AcceptanceTest.sadFailed, A2AcceptanceTest.extraCreditFailed)                
        except:
            log.info('test number invalid ... ignored')
        if self.errored:
            log.info('\tERRORED -----')
        elif self.failed:
            log.info('\tFAILED -----')
        else:
            log.info('\tPASSED -----')
            
#-------------------------------------------------------------------------------
# Analysis
#    _check(value)
#
#    inputs:
#        parms:        dictionary; mandatory; arrives validated
#        parms['op']    string; "check"; mandatory; arrives validated
#        parms['cube']  string; 54 characters, [azAZ09], 
#                               9 occurrences of 6 characters, 
#                               middle face is each of 6 characters;
#                               mandatory; arrives unvalidated
#
#    outputs:
#        side-effects:  no state change; no external effects
#        returns:  dictionary
#            nominal:
#                dictionary['cube']        same description as parms['cube']
#                dictionary['status']      'ok'
#            abnormal:
#                dictionary['status']      'error: xxx' where xxx is dev-selected message, len>0
#
#    confidence level:  boundary value analysis
#
#    happy path:
#        test 010:  solved cube consisting of traditional colors
#        test 020:  solved cube consisting of traditional colors but not in traditional orientation
#        test 030:  solved cube consisting of nontraditional
#        test 040:  nominal scrambled cube
#        test 050:  extraneous keys
#        test 060:  exactly one key returned
#
#    sad path:
#        test 910:  missing cube
#        test 920:  short cube
#        test 930:  long cube
#        test 940:  cube with illegal characters, valid otherwise
#        test 950:  cube with != 9 occurrences of at least one of 6 unique characters
#        test 960:  cube with more than 6 unique characters
#        test 970:  cube non-unique middle face
#        test 980:  exactly one key returned
#
#        test 990:  extra credit:  cube with contradictory corner
#        test 995:  extra credit:  cube with contradictory edge
#

    def testA2_check_010_ShouldReturnOKOnTraditionalSolvedCube(self):
        #        test 010:  solved cube
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = 'ok'
        
        actualResult = check._check(inputDict)
        self.assertEqual(expectedResult, actualResult.get('status'),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_020_ShouldReturnOKOnNonTraditionalSolvedCube(self):
        #    test 020:  solved cube consisting of traditional colors but not in traditional orientation
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'gggggggggwwwwwwwwwyyyyyyyyybbbbbbbbbrrrrrrrrrooooooooo'
        
        expectedResult = 'ok'
        
        actualResult = check._check(inputDict)
        self.assertEqual(expectedResult, actualResult.get('status'),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_030_ShouldReturnOKOnNonTraditionalColoredCube(self):
        #    test 030:  solved cube consisting of nontraditional
        inputDict = {'op': 'check'}
        inputDict['cube'] = '111111111AAAAAAAAA333333333aaaaaaaaa999999999zzzzzzzzz'
        
        expectedResult = 'ok'
        
        actualResult = check._check(inputDict)
        self.assertEqual(expectedResult, actualResult.get('status'),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_040_ShouldReturnOKOnScrambledCube(self):
        #    test 040:  nominal scrambled cube
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'rbbgbobbgrgwyrywyobggrggywgoryyowowwyoobyrgwyrorrwbwob'
        
        expectedResult = 'ok'
        
        actualResult = check._check(inputDict)
        self.assertEqual(expectedResult, actualResult.get('status'),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_050_ShouldReturnOKOnExtraneous(self):
        #    test 050:  extraneous keys
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['bogus'] = 'this is a bogus key'
        
        expectedResult = 'ok'
        
        actualResult = check._check(inputDict)
        self.assertEqual(expectedResult, actualResult.get('status'),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_060_ShouldReturnOKOnSingleReturnKey(self):
        #    test 060:  exactly one key returned
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = 1
        
        actualResult = check._check(inputDict)
        self.assertEqual(expectedResult, len(actualResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_910_ShouldErrOnMissingCube(self):
        #    test 910:  missing cube
        inputDict = {'op': 'check'}
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_920_ShouldErrOnShortCube(self):
        #    test 920:  short cube
        inputDict = {'op': 'check'}
        inputDict['cube'] = ''
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_930_ShouldErrOnLongCube(self):
        #    test 930:  long cube
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_940_ShouldErrOnIllegalCharacters(self):
        #    test 940:  cube with illegal characters, valid otherwise
        inputDict = {'op': 'check'}
        inputDict['cube'] = '         rrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_950_ShouldErrOnNon9OccurrencesOfCharacters(self):
        #    test 950:  cube with != 9 occurrences of at least one of 6 unique characters
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrbbbbbbbbboooooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_960_ShouldErrOnNon6UniqueCharacters(self):
        #    test 960:  cube with more than 6 unique characters
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwp'
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_970_ShouldErrOnNonUniqueMiddleFaces(self):
        #    test 970:  cube non-unique middle face
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbwrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwbwwww'
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_980_ShouldErrWithOnlyOneKeyReturned(self):
        #    test 980:  exactly one key returned
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
        
        expectedResult = 1
        
        actualResult = check._check(inputDict)
        self.assertEqual(expectedResult, len(actualResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------


    def testA2_check_990_ExtraCredit_ShouldErrWithContradictoryCorner(self):
        #    test 990:  extra credit:  cube with contradictory corner
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrggggggoggoogooooooyyyyyyyyywwwwwwwww'
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
    def testA2_check_995_ExtraCredit_ShouldErrWithContradictoryCorner(self):
        #    test 995:  extra credit:  cube with contradictory edge
        inputDict = {'op': 'check'}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggooowoooooyyyyyyyyywwwwwowww'
        
        expectedResult = 'error:'
        
        actualResult = check._check(inputDict)
        self.assertTrue(actualResult.get('status',"").startswith(expectedResult),
                        'fail: ' + inspect.currentframe().f_code.co_name)
# ------------------------------------------
if __name__ == "__main__":
    try:
        print(" ")
        print("@A2   " + os.environ["id"])
        print("      " + os.environ["name"])        
        # print("      " + os.environ["url"])
        print("      " + str(datetime.datetime.now()))
        print("+------------------------------------------------------------------")    
    except:
        print("@A2  -- identifying information missing")
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
    log.info("@A2  " + os.environ["id"])
    log.info("      " + os.environ["name"])        
    # log.info("      " + os.environ["url"])
    log.info("      " + str(datetime.datetime.now()))
    
    unittest.main()
