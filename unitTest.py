import unittest
import cli
from importlib import reload

class TestCliMethods(unittest.TestCase):

    # testing the condition when only the course code is inputed and the other fields are empty.
    def testOnlyCode(self):
        test_string = 'cis*3110'
        check_value = cli.courseSearch([test_string, 'x', 'x', 'x'])
        self.assertEqual(check_value, [{'cc': 'CIS*3110', 'cred': '[0.50]', 'desc': 'Operating Systems I', 'off': 'Winter Only', 'preqArr': [{'preq': 'CIS*2520', 'type': 'mand'}, {'preq': ' (CIS*2030 or ENGG*2410).', 'type': 'or'}]}])

    # testing the condition when only the year is inputed and the other fields are empty.
    def testOnlyYear(self):
        cli.openCourses()
        cli.unit_test = True
        tot = 0
        for element in cli.courses:
            if (element['cc'].split("*", 1)[1])[0] == '3':
                tot+=1
        check_value = cli.courseSearch(['x', '3', 'x', 'x']) 
        self.assertEqual(len(check_value), tot)

    # testing the condition when only the credit is inputed and the other fields are empty.
    def testOnlyCredit(self):
        cli.openCourses()
        cli.unit_test = True
        tot = 0
        for element in cli.courses:
            if element['cred'] == '[0.75]':
                tot+=1
        check_value = cli.courseSearch(['x', 'x', '0.75', 'x'])
        self.assertEqual(len(check_value), tot)

    # testing the condition when only the semester is inputed and the other fields are empty.
    def testOnlySemester(self):
        cli.openCourses()
        cli.unit_test = True
        tot = 0
        for element in cli.courses:
            if ("Winter" in element['off']):
                tot+=1
        check_value = cli.courseSearch(['x', 'x', 'x', 'Winter'])
        self.assertEqual(len(check_value), tot)

    # testing the condition when all the fields are full.
    def testFilled(self):
        cli.openCourses()
        cli.unit_test = True
        check_value = cli.courseSearch(['BIOL*4900', '4', '0.50', 'fall'])
        self.assertEqual(check_value, [{'cc': 'BIOL*4900', 'cred': '[0.50]', 'desc': 'Field Biology', 'off': 'Summer, Fall, and Winter', 'preqArr': [{'preq': 'BIOL*2060', 'type': 'mand'}]}])

    # testing whether the course filter function correctly filters a course.
    def testCourseFilter(self):
        cli.openCourses()
        cli.unit_test = True
        cli.code = 'cis*2750'
        course_code = cli.check_code
        self.assertEqual(cli.filterCode(course_code,cli.courses), [{'cc': 'CIS*2750', 'cred': '[0.75]', 'desc': 'Software Systems Development and Integration', 'off': 'Winter Only', 'preqArr': [{'preq': 'CIS*2520', 'type': 'mand'}, {'preq': ' (CIS*2430 or ENGG*1420)', 'type': 'or'}]}])
        reload(cli)
    
    # testing whether the credit filter function correctly filters a credit.
    def testCreditFilter(self):
        cli.openCourses()
        cli.unit_test = True
        cli.credit_count = '0.75'
        credit = cli.check_credit
        tot = 0
        for element in cli.courses:
            if element['cred'] == '[0.75]':
                tot+=1
        self.assertEqual(len(cli.filterCredit(credit,cli.courses)), tot)
        reload(cli)
    
    # testing whether the year fitler function correctly filters a year.
    def testYearFilter(self):
        cli.openCourses()
        cli.year = '4'
        cli.unit_test = True
        year = cli.check_year
        tot = 0
        for element in cli.courses:
            if (element['cc'].split("*", 1)[1])[0] == '4':
                tot+=1
        self.assertEqual(len(cli.filterYear(year,cli.courses)), tot)
        reload(cli)
    
    # testing whether the semester fitler function correctly filters a semester.
    def testSemesterFilter(self):
        cli.openCourses()
        cli.unit_test = True
        cli.semester = 'Summer'
        semester = cli.check_semester
        tot = 0
        for element in cli.courses:
            if ("Summer" in element['off']):
                tot+=1
        self.assertEqual(len(cli.filterSemester(semester,cli.courses)), tot)
        reload(cli)

    # testing if the check course function correctly checks for a valid course.
    def testCheckCourse(self):
        cli.openCourses()
        cli.unit_test = True
        cli.code = 'cis*2750'
        self.assertTrue(cli.check_code)
        reload(cli)

    # testing if the check course credit function correctly checks for a valid credit.
    def testCheckCredit(self):
        cli.openCourses()
        cli.unit_test = True
        cli.credit_count = '0.50'
        self.assertTrue(cli.credit_count)
        reload(cli)
    
    # testing if the check year function correctly checks for a valid year.
    def testCheckYear(self):
        cli.openCourses()
        cli.unit_test = True
        cli.year = '2'
        self.assertTrue(cli.check_year)
        reload(cli)
    
    # testing if the check semester function correctly checks for a valid semester.
    def testCheckSemester(self):
        cli.openCourses()
        cli.unit_test = True
        cli.semester = 'Fall'
        self.assertTrue(cli.check_semester)
        reload(cli)

if __name__ == '__main__':
    unittest.main()