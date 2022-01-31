import unittest
import cli

class TestCliMethods(unittest.TestCase):

    def testCourseCode(self):
        cli.openCourses()
        cli.code = 'cis*2750'
        course_code = cli.check_code
        self.assertEqual(cli.filterCode(course_code,cli.courses), [{'cc': 'CIS*2750', 'cred': '[0.75]', 'desc': 'Software Systems Development and Integration', 'off': 'Winter Only', 'preqArr': [{'preq': 'CIS*2520', 'type': 'mand'}, {'preq': ' (CIS*2430 or ENGG*1420)', 'type': 'or'}]}])

    def testOnlyCode(self):
        test_string = 'cis*3110'
        check_value = cli.courseSearch([test_string, 'x', 'x', 'x'])
        self.assertEqual(check_value, [{'cc': 'CIS*3110', 'cred': '[0.50]', 'desc': 'Operating Systems I', 'off': 'Winter Only', 'preqArr': [{'preq': 'CIS*2520', 'type': 'mand'}, {'preq': ' (CIS*2030 or ENGG*2410).', 'type': 'or'}]}])

    def testOnlyYear(self):
        cli.openCourses()
        tot = 0
        for element in cli.courses:
            if (element['cc'].split("*", 1)[1])[0] == '3':
                tot+=1
        check_value = cli.courseSearch(['x', '3', 'x', 'x']) 
        self.assertEqual(len(check_value), tot)
    
    def testOnlyCredit(self):
        cli.openCourses()
        tot = 0
        for element in cli.courses:
            if element['cred'] == '[0.75]':
                tot+=1
        check_value = cli.courseSearch(['x', 'x', '0.75', 'x'])
        self.assertEqual(len(check_value), tot)
    
    def testOnlySemester(self):
        cli.openCourses()
        tot = 0
        for element in cli.courses:
            if ("Winter" in element['off']):
                tot+=1
        check_value = cli.courseSearch(['x', 'x', 'x', 'Winter'])
        self.assertEqual(len(check_value), tot)
    
    def testFilled(self):
        check_value = cli.courseSearch(['ZOO*3700', '3', '0.50', 'fall'])
        print(check_value)
        self.assertEqual(check_value, [{'cc': 'ZOO*3700', 'cred': '[0.50]', 'desc': 'Integrative Biology of Invertebrates', 'off': 'Fall Only', 'preqArr': [{'preq': 'ZOO*2700', 'type': 'mand'}]}])


if __name__ == '__main__':
    unittest.main()