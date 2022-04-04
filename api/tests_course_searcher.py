#
# Author: Team 10
# Course: CIS*3760
# Date: 7 Feb 2022
# Description: unit tests for course_searcher
#

import unittest
import course_searcher
from importlib import reload

# search course tests
class test_search_course(unittest.TestCase):
    def test_search_course_cis3110_x_x_x_is_course(self):
        test_string = 'cis*3110'
        check_value = course_searcher.search_course([test_string, 'x', 'x', 'x'])
        self.assertEqual(check_value, [{'cc': 'CIS*3110', 'cred': '[0.50]', 'desc': 'Operating Systems I', 'off': 'Winter Only', 'preqArr': [{'preq': 'CIS*2520', 'type': 'mand'}, {'preq': ' (CIS*2030 or ENGG*2410).', 'type': 'or'}]}])

    def test_course_search_x_3_x_x_is_correct(self):
        course_searcher.open_courses()
        tot = 0
        for element in course_searcher.courses:
            if (element['cc'].split("*", 1)[1])[0] == '3':
                tot+=1
        check_value = course_searcher.search_course(['x', '3', 'x', 'x']) 
        self.assertEqual(len(check_value), tot)

    def test_search_course_x_x_75_x_is_correct(self):
        course_searcher.open_courses()
        tot = 0
        for element in course_searcher.courses:
            if element['cred'] == '[0.75]':
                tot+=1
        check_value = course_searcher.search_course(['x', 'x', '0.75', 'x'])
        self.assertEqual(len(check_value), tot)

    def test_search_course_x_x_x_Winter_is_correct(self):
        course_searcher.open_courses()
        tot = 0
        for element in course_searcher.courses:
            if ("Winter" in element['off']):
                tot+=1
        check_value = course_searcher.search_course(['x', 'x', 'x', 'Winter'])
        self.assertEqual(len(check_value), tot)

    def test_search_course_biol4900_4_50_fall_is_course(self):
        course_searcher.open_courses()
        check_value = course_searcher.search_course(['BIOL*4900', '4', '0.50', 'fall'])
        self.assertEqual(check_value, [{'cc': 'BIOL*4900', 'cred': '[0.50]', 'desc': 'Field Biology', 'off': 'Summer, Fall, and Winter', 'preqArr': [{'preq': 'BIOL*2060', 'type': 'mand'}]}])


# filter tests
class test_filters(unittest.TestCase):
    def test_filter_code_cis2750_is_course(self):
        course_searcher.open_courses()
        course_searcher.code = 'cis*2750'
        course_code = course_searcher.check_code
        self.assertEqual(course_searcher.filter_code(course_code,course_searcher.courses), [{'cc': 'CIS*2750', 'cred': '[0.75]', 'desc': 'Software Systems Development and Integration', 'off': 'Winter Only', 'preqArr': [{'preq': 'CIS*2520', 'type': 'mand'}, {'preq': ' (CIS*2430 or ENGG*1420)', 'type': 'or'}]}])
        reload(course_searcher)
    
    def test_filter_weight_75_is_correct(self):
        course_searcher.open_courses()
        course_searcher.weight = '0.75'
        weight = course_searcher.check_weight
        tot = 0
        for element in course_searcher.courses:
            if element['cred'] == '[0.75]':
                tot+=1
        self.assertEqual(len(course_searcher.filter_weight(weight,course_searcher.courses)), tot)
        reload(course_searcher)
    
    def test_filter_year_4_is_correct(self):
        course_searcher.open_courses()
        course_searcher.year = '4'
        year = course_searcher.check_year
        tot = 0
        for element in course_searcher.courses:
            if (element['cc'].split("*", 1)[1])[0] == '4':
                tot+=1
        self.assertEqual(len(course_searcher.filter_year(year,course_searcher.courses)), tot)
        reload(course_searcher)
    
    def test_filter_semester_summer_is_correct(self):
        course_searcher.open_courses()
        course_searcher.semester = 'Summer'
        semester = course_searcher.check_semester
        tot = 0
        for element in course_searcher.courses:
            if ("Summer" in element['off']):
                tot+=1
        self.assertEqual(len(course_searcher.filter_semester(semester,course_searcher.courses)), tot)
        reload(course_searcher)

# checker (comparator) tests
class test_checkers(unittest.TestCase):
    def test_check_code_cis2750_is_true(self):
        course_searcher.open_courses()
        course_searcher.code = 'cis*2750'
        self.assertTrue(course_searcher.check_code)
        reload(course_searcher)
        
    def test_check_weight_50_is_true(self):
        course_searcher.open_courses()
        course_searcher.weight = '0.50'
        self.assertTrue(course_searcher.weight)
        reload(course_searcher)
    
    def test_check_year_2_is_true(self):
        course_searcher.open_courses()
        course_searcher.year = '2'
        self.assertTrue(course_searcher.check_year)
        reload(course_searcher)
    
    def test_check_semester_fall_is_true(self):
        course_searcher.open_courses()
        course_searcher.semester = 'Fall'
        self.assertTrue(course_searcher.check_semester)
        reload(course_searcher)

if __name__ == '__main__':
    unittest.main()