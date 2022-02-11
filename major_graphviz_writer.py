#
# Author: Team 10
# Course: CIS*3760
# Date: 7 Feb 2022
# Description: a library to create a graph(viz) file given a major
#

import json
import re
import os

courses_list = []
#text_file_name = "output.txt"
text_file_name = "output.dot"
# Flag used to prevent using repeated courses from scraper
#flag_course = 0

def read_reqs(req_array, course_code):
    # Going through pre-requisites list
    for req in req_array:
    
        # Dictionaries to store pre-requisite information
        req_type = req['type']
        req_name = req['preq']
    
        # Making sure pre-requisite isn't blank
        if req_name == " ":
            break
            
        # Removing excess white spaces
        req_name = req_name.strip()
    
        # Dealing with "mand" types
        if req_type == "mand" :
            # Dealing with credit pre-requisites
            if "credit" in req_name:
    
                # Deciding not to graph if they do not specify credits in what, may change.
    
                if " in " in req_name:
                    # Creating string
                    graph_string = "\"" + req_name + "\" -> \"" + course_code + "\""
                    write_to_file(graph_string)
                #else:
                    #graph_string = "skip"
                        
            else:
                # Removing unnecessary brackets
                req_name = req_name.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    
                num_courses = req_name.count("*")
                    
                # If more than 1 course is present
                if num_courses > 1:
                    course_string = req_name.split(" ")
    
                    # Looping through text
                    for i in range(0, len(course_string)) :
                        if "*" in course_string[i]:
                            # Creating string
                            graph_string = "\"" + course_string[i] + "\" -> \"" + course_code + "\" [style=solid]"
                            write_to_file(graph_string)
                else:
                    # Creating string
                    graph_string = "\"" + req_name + "\" -> \"" + course_code + "\" [style=solid]"
                    write_to_file(graph_string)

        # Dealing with "or" type
        elif req_type == "or":
            if "OR" in req_type:
                req_type.replace("OR", "or")

            # Checking for "including" cases
            if "including" in req_name:
                split_including = req_name.split(" including ")
    
                if len(split_including) > 1:
                    req_name = split_including[1]
    
            # Removing unnecessary brackets
            req_name = req_name.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    
            # Splitting by "or"
            split_name = req_name.split(" or ")
            num_courses = len(split_name)
    
            # For loop to go through courses
            for i in range (0, num_courses):
                # Removing excess white spaces
                split_name[i] = split_name[i].strip()
                if(split_name[i] != "equivalent"):
                    graph_string = "\"" + split_name[i] + "\" -> \"" + course_code + "\" [style=dashed]"
                    write_to_file(graph_string)
    
        # Dealing with "num_of" type
        elif req_type == "numOf":
            req_name = req_name.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    
            if " of " in req_name:
                split_of = req_name.split(" of ")
                num_splits = len(split_of)

                # If list includes course code
                if "*" in split_of[1]:
                    # For loop to search through string for "# of" format
                    for i in range(0, num_splits):
    
                        length = len(split_of[i])
    
                        # First iteration, extract number
                        if i == 0:
                            num_of = split_of[i][length - 1]
                            
                        # Otherwise, extract courses
                        else:
    
                            # Extracting number for next iteration
                            if(i != num_splits - 1):
                                courses_of = split_of[i]
                                courses_of = courses_of.split(" ")
                                num_courses_of = len(courses_of)
    
                                # Looping through courses
                                for j in range (0, num_courses_of):
                                    # If current word is a course
                                    if("*" in courses_of[j]):
                                        graph_string = "\"" + courses_of[j] + "\" -> \"" + course_code + "\" [style=dashed] [label=\"" + num_of + " of\"]"
                                        write_to_file(graph_string)

                                num_of = split_of[i][length - 1]
    
                            else:
                                courses_of = split_of[i]
                                courses_of = courses_of.split(" ")
                                num_courses_of = len(courses_of)
    
                                # Looping through courses
                                for j in range (0, num_courses_of):
                                    # If current word is a course
                                    if("*" in courses_of[j]):
                                        graph_string = "\"" + courses_of[j] + "\" -> \"" + course_code + "\" [style=dashed] [label=\"" + num_of + " of\"]"
                                        write_to_file(graph_string)
                # If list does not include course code
                else:
                    graph_string = "\"" + req_name + "\" -> \"" + course_code + "\" [style=solid]"
                    write_to_file(graph_string)

        # Dealing with "recommended" type:        
        elif req_type == "rec":
            # Removing unnecessary brackets
            req_name = req_name.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    
            # Splitting string by spaces
            split_rec = req_name.strip().split(" ")
    
            graph_string = "\"" + split_rec[0] + "\" -> \"" + course_code + "\" [style=solid] [label=\"recommended\"]"
            write_to_file(graph_string)

def read_courses(c_code):
    f = open('courses.json')
    
    # Loading json file
    courses = json.load(f)
    
    
    # For loop to go through courses
    for course in courses:
        if(c_code == course['cc']):
            # Plotting course code alone
            write_to_file("\"" + course['cc'] + "\"")

            # Creating array to store pre-requisites
            req_array = course['preqArr']

            read_reqs(req_array, course['cc'])

    #print(courses_list)
    f.close()

# Function used to write each mapping to its corresponding DOT file
def write_to_file(mapping):

    # If mapping is already found in text file, exit
    with open(text_file_name, "r") as text_file:
        if mapping in text_file.read():
            return 0

    with open(text_file_name, "a") as text_file:
        text_file.write(mapping + "\n")

# Function used to parse major data stored in json file using major input
def read_major(major_code):
    f = open('programs.json')
    major_list = json.load(f)
    
    # clear output file
    open(text_file_name, 'w').close()

    # Writing heading of dot file
    with open(text_file_name, "a") as text_file:
        text_file.write("digraph CourseMap {\n")

    # Flag initialization
    flag = 0

    # For loop to go through each course code in major
    for item in major_list:
        m_code = re.search(r"\((.*?)\)", item['program'])

        if(major_code == m_code.group(1)):
            flag = 1
            course_array = item['reqs']

            # For loop to traverse course array
            for course_code in course_array:

                # Removing unkown character
                if "or " in course_code:
                    course_code = course_code.replace("or ", "")
                
                read_courses(course_code)

            
            # Breaking outer for loop to ensure no other matches with majors are made
            break
        
    if(flag == 0):
        print("Major not found!")
    
    # Closing bracket of dot file
    with open(text_file_name, "a") as text_file:
        text_file.write("}\n")

    # Graphing command
    cmd = "dot -Tpdf " + text_file_name + " > output.pdf"
    os.system(cmd)

    
    

def main():
    m_code = "hi"
    while m_code != "exit":
        print("Please enter major code:")
        m_code = input()

        if m_code != "exit":
            read_major(m_code)

if __name__ == "__main__":
    main()
