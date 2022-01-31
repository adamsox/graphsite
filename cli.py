#
# CIS*3760 
# Team 10
# 23 Jan 2022
# Program allowing user to search courses database using command-line interface
#

#Importing required objects
import json

# List of courses from the courses.json file
courses = []
unit_test = False

# Main
def main():
    #Setting exit boolean to be false by default.
    exit = False

    # Taking user input until user inputs exit command.
    while not(exit):
        print('coursesearch: ', end="")
        val = input()
        val = val.lower()
        # spliting the user inputed string by the whitespaces and populating a list with those values.
        arguments = val.split()

        # If user enters blank string as input.
        if val == "":
            print("Critical Error please input a valid command!")
            return None

        # If user quits/exits program.
        if val == "exit" or val == "quit" or val == "q":
            exit = True

        elif len(arguments) == 4:
            courseSearch(arguments)
            print()

        # If user enters a command other than exit or coursesearch.
        else:
            print("usage: coursesearch course_code course_year credit_count season")
            print("Put \'x\' for anything you do not wish to specify.")
            print ("e.g., 'coursesearch: cis 3 0.75 f' searches for a cis 3rd year 0.75 fall course")
            print ("e.g., 'coursesearch: hist x 1.00 x' searches for a hist 1.00 course regardless of year or semester")
            # return None
    return None

# Initializing variables
code = ""
year = ""
credit_count = ""
semester = ""

# Checking if a course matches the requested code
def check_code(course):    
    if code.lower() in course['cc'].lower():
        return True
    else:
        return False

# Checking if a course matches the requested year
def check_year(course):
    course_year = (course['cc'].split("*", 1)[1])
    
    if year == course_year[0]:
        return True
    else:
        return False

# Checking if a course matches the requested credits
def check_credit(course):
    if credit_count in course['cred']:
        return True
    else:
        return False

# Checking if a course matches the requested semester
def check_semester(course):
    sem = semester.lower()
    
    #  if in USER REQUEST and COURSE
    if ("winter" in sem or "w" in sem) and ("Winter" in course['off']):
        return True
    elif ("summer" in sem or "s" in sem) and ("Summer" in course['off']):
        return True
    elif ("fall" in sem or "f" in sem) and ("Fall" in course['off']):
        return True
    else:
        return False
        
# courseSearch function
def courseSearch(args_list):

    # case where the only argument is the program name
    if len(args_list) < 4 or len(args_list) > 4:
        print("usage: coursesearch course_code course_year credit_count season")
        print("Put \'x\' for anything you do not wish to specify.")
        print ("e.g., 'coursesearch: cis 3 0.75 f' searches for a cis 3rd year 0.75 fall course")
        print ("e.g., 'coursesearch: hist x 1.00 x' searches for a hist 1.00 course regardless of year or semester")
    else:
        global code, year, credit_count, semester
        code = args_list[0]
        year = args_list[1]
        credit_count = args_list[2]
        semester = args_list[3]

        # Filtering course list
        filtered_courses = courses
        # Code
        if code != "x":
            filtered_courses = filterCode(check_code, filtered_courses)
        # Year
        if year != "x":
            filtered_courses = filterYear(check_year, filtered_courses)
        
        # Credits
        if credit_count != "x":
            filtered_courses = filterCredit(check_credit, filtered_courses)
        
        # Semester
        if semester != "x":
            filtered_courses = filterSemester(check_semester, filtered_courses)
        #print(filtered_courses)
        if not filtered_courses:
            print("No results found")
        else:
            filtered_courses = sorted(filtered_courses, key=lambda x : x['cc'])
            for course in filtered_courses:
                if unit_test == False:
                    print(str(course['cc']) + " " + str(course['cred']) + " " + str(course['desc']) + " " +  str(course['off']))
            return filtered_courses

def filterCode(check_code, filtered_courses):
    courses_iterator = filter(check_code, filtered_courses)
    filtered_courses = list(courses_iterator)
    return filtered_courses

def filterCredit(check_credit, filtered_courses):
    courses_iterator = filter(check_credit, filtered_courses)
    filtered_courses = list(courses_iterator)
    return filtered_courses

def filterYear(check_year, filtered_courses):
    courses_iterator = filter(check_year, filtered_courses)
    filtered_courses = list(courses_iterator)
    return filtered_courses

def filterSemester(check_semester, filtered_courses):
    courses_iterator = filter(check_semester, filtered_courses)
    filtered_courses = list(courses_iterator)
    return filtered_courses


# This function opens the courses.json file and takes its contents
def openCourses():
    with open("courses.json", "r") as file:
        jsonData = json.load(file)

    for i in jsonData:
        courses.append(i)
    
    return None


if __name__ == "__main__":
    print("Close the program by inputing exit or search for a course by inputing coursesearch.\n")
    print("usage: coursesearch: course_code course_year credit_count season")
    print("Put x for anything you do not wish to specify.")
    print ("e.g., 'coursesearch: cis 3 0.75 f' searches for a cis 3rd year 0.75 fall course")
    print ("e.g., 'coursesearch: hist x 1.00 x' searches for a hist 1.00 course regardless of year or semester")
    openCourses()
    main()
