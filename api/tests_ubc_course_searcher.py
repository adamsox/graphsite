#
# Author: Team 10
# Course: CIS*3760
# Date: 4 April 2022
# Description: unit tests for the UBC ubc_course_searcher
#

import unittest
import ubc_course_searcher
from importlib import reload

# search course tests
class test_search_course(unittest.TestCase):
    def test_search_course_cis3110_x_x_x_is_course(self):
        test_string = 'AANB500'
        check_value = ubc_course_searcher.search_ubc([test_string, 'x', 'x'])
        self.assertEqual(check_value, [{'cc': 'AANB500', 'cred': '(3)', 'desc': ' Graduate Seminar ', 'all_preq': ''}, {'cc': 'AANB500', 'cred': '(3)', 'desc': ' Graduate Seminar ', 'all_preq': ''}])
        

    def test_search_course_x_x_3_x_is_correct(self):
        ubc_course_searcher.open_courses()
        tot = 0
        for element in ubc_course_searcher.courses:
            if element['cred'] == '(2-6)':
                tot+=1
        check_value = ubc_course_searcher.search_ubc(['x', 'x', '(2-6)'])
        self.assertEqual(len(check_value), tot)


    def test_search_course_biol4900_4_50_fall_is_course(self):
        ubc_course_searcher.open_courses()
        check_value = ubc_course_searcher.search_ubc(['AANB504', '5', '(3)'])
        self.assertEqual(check_value, [{'cc': 'AANB504', 'cred': '(3)', 'desc': ' Research Methodology in Applied Animal Biology ', 'all_preq': ''}, {'cc': 'AANB504', 'cred': '(3)', 'desc': ' Research Methodology in Applied Animal Biology ', 'all_preq': ''}])


# filter tests
class test_filters(unittest.TestCase):
    def test_filter_code_AANB500_is_course(self):
        ubc_course_searcher.open_courses()
        ubc_course_searcher.code = 'AANB500'
        course_code = ubc_course_searcher.check_code
        self.assertEqual(ubc_course_searcher.filter_code(course_code,ubc_course_searcher.courses), [{'cc': 'AANB500', 'cred': '(3)', 'desc': ' Graduate Seminar ', 'all_preq': ''}, {'cc': 'AANB500', 'cred': '(3)', 'desc': ' Graduate Seminar ', 'all_preq': ''}])
        reload(ubc_course_searcher)
    
    def test_filter_weight_3_is_correct(self):
        ubc_course_searcher.open_courses()
        ubc_course_searcher.weight = '(3)'
        weight = ubc_course_searcher.check_weight
        tot = 0
        for element in ubc_course_searcher.courses:
            if element['cred'] == '(3)':
                tot+=1
        self.assertEqual(len(ubc_course_searcher.filter_weight(weight,ubc_course_searcher.courses)), tot)
        reload(ubc_course_searcher)

# checker (comparator) tests
class test_checkers(unittest.TestCase):
    def test_check_code_AANB500_is_true(self):
        ubc_course_searcher.open_courses()
        ubc_course_searcher.code = 'AANB500'
        self.assertTrue(ubc_course_searcher.check_code)
        reload(ubc_course_searcher)
        
    def test_check_weight_50_is_true(self):
        ubc_course_searcher.open_courses()
        ubc_course_searcher.weight = '(3/6)'
        self.assertTrue(ubc_course_searcher.weight)
        reload(ubc_course_searcher)
    
    def test_check_year_2_is_true(self):
        ubc_course_searcher.open_courses()
        ubc_course_searcher.year = '2'
        self.assertTrue(ubc_course_searcher.check_year)
        reload(ubc_course_searcher)

if __name__ == '__main__':
    unittest.main()