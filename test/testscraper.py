import unittest
import os

class TestScraper(unittest.TestCase):
    
    # Testing link scraper
    def testLinks(self):
        os.system('node linkscraper.js > test_linkoutput.txt')

        # Testing for Psychology program link
        f = open('test_linkoutput.txt')
        self.assertIn('https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/psyc/',f.read())
        f.close()

        # Testing for Music program link
        f = open('test_linkoutput.txt')
        self.assertIn('https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/musc/',f.read())
        f.close()

    
    # testing that first course is scraped
    def testFirstCourseScraper(self):
        os.system('node course_scraper_test.js > test_singlecourse.txt')

        f = open('test_singlecourse.txt')
        self.assertIn('cc: \'MATH*1030\'',f.read())
        f.close()

    # testing that last course is scraped
    def testLastCourse(self):
        f = open('test_singlecourse.txt')
        self.assertIn('cc: \'MATH*4600\'',f.read())
        f.close()

if __name__ == '__main__':
    unittest.main()