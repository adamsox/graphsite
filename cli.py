#
# CIS3760_Team 10
# cli.py
# 23 Jan 2022
#

import json

# list of courses from the courses.json file
courses = []

def main():
    exit = False

    # taking user input until user inputs exit command.
    while not(exit):
        val = input()
        # spliting the user inputed string by the whitespaces and populating a list with those values.
        arguments = val.split()
        print(val)

        if val == "":
            print("Error please input a valid command")
            return None

        if val == "exit":
            exit = True

        elif arguments[0] == "coursesearch":
            courseSearch(arguments)

        # case where the user inputs a command other than exit or coursesearch.
        else:
            print("Error please input a valid command")
            return None
    return None

code = ""
year = ""
credit_count = ""
semester = ""

# checks if a course matches the requested code
def check_code(course):    
    if code.lower() in course['cc'].lower():
        return True
    else:
        return False

# checks if a course matches the requested year
def check_year(course):
    course_year = (course['cc'].split("*", 1)[1])
    
    if year == course_year[0]:
        return True
    else:
        return False

# checks if a course matches the requested credits
def check_credit(course):
    if credit_count in course['cred']:
        return True
    else:
        return False

# checks if a course matches the requested semester
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
        

def courseSearch(args_list):

    # case where the only argument is the program name
    if len(args_list) < 5 or len(args_list) > 5:
        print("usage: coursesearch course_code course_year credit_count season")
        print("Put x for anything you do not wish to specify.")
        print ("e.g., 'coursesearch cis 3 0.75 f' searches for a cis 3rd year 0.75 fall course")
        print ("e.g., 'coursesearch hist x 1.00 x' searches for a hist 1.00 course regardless of year or semester")
    else:
        global code, year, credit_count, semester
        code = args_list[1]
        year = args_list[2]
        credit_count = args_list[3]
        semester = args_list[4]

        # filtering course list
        filtered_courses = courses
        # code
        if code != "x":
            courses_iterator = filter(check_code, filtered_courses)
            filtered_courses = list(courses_iterator)
        
        # year
        if year != "x":
            courses_iterator = filter(check_year, filtered_courses)
            filtered_courses = list(courses_iterator)
        
        # credits
        if credit_count != "x":
            courses_iterator = filter(check_credit, filtered_courses)
            filtered_courses = list(courses_iterator)
        
        # semester
        if semester != "x":
            courses_iterator = filter(check_semester, filtered_courses)
            filtered_courses = list(courses_iterator)
        #print(filtered_courses)
        if not filtered_courses:
            print("No results found")
        else:
            #print(filtered_courses)
            
            for course in filtered_courses:
                print(str(course['cc']) + " " + str(course['cred']) + " " + str(course['desc']) + " " +  str(course['off']))



# This function opens the courses.json file and takes its contents
def openCourses():
    with open("courses.json", "r") as file:
        jsonData = json.load(file)

    for i in jsonData:
        courses.append(i)
    
    return None


if __name__ == "__main__":
    print("Close the program by inputing exit or search for a course by inputing coursesearch.\n")
    print("usage: coursesearch course_code course_year credit_count season")
    print("Put x for anything you do not wish to specify.")
    print ("e.g., 'coursesearch cis 3 0.75 f' searches for a cis 3rd year 0.75 fall course")
    print ("e.g., 'coursesearch hist x 1.00 x' searches for a hist 1.00 course regardless of year or semester")
    openCourses()
    main()