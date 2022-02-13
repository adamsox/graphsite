#
# Author: Team 10
# Course: CIS*3760
# Date: 12 Feb 2022
# Description: a library to create a graph(viz) file given a course
#              prefix or code
#

import json
import re
import os

courses_list = []
text_file_name = "output.dot"

# Function used to write each mapping to its corresponding DOT file
def write_to_file(mapping):

    # If mapping is already found in text file, exit
    with open(text_file_name, "r") as text_file:
        if mapping in text_file.read():
            return 0

    with open(text_file_name, "a") as text_file:
        text_file.write(mapping + "\n")

def fix_course_codes(preq_str):
    word_array = preq_str.split(" ")
    size = len(word_array)
    final_str = ""

    # Going through each word in description
    for i in range(0, size):

        # If word is upper case
        if word_array[i].isupper() == True:

            # If we are not at end of description
            if i != size - 1:
                word_str = word_array[i + 1]
                # Replacing commas and fullstops
                #word_str = word_str.replace(",", "")
                word_str = word_str.replace(".", "")
                word_str = word_str.replace(",", "")

                word_str = word_str.strip()

                # If following word is numeric and 3 characters long
                if word_str.isdigit() == True:
                    if len(word_str) == 3:
                        word_array[i] = word_array[i] + "*" + word_str
                        word_array[i + 1] = ""

        final_str = final_str + " " + word_array[i]
    final_str = final_str.strip()
    
    return final_str

# Function to determine type of pre-requisites for course
def type_find(preq_str, c_code):
    preq_str = fix_course_codes(preq_str)
    #print(preq_str)

    if "all of" in preq_str.lower():
        all_of_array = preq_str.lower().split("all of")
        all_of_len = len(all_of_array)

        for i in range(0, all_of_len):
            if "*" in all_of_array[i]:
                spaces_array = all_of_array[i].split(" ")
                spaces_len = len(spaces_array)

                for j in range(0, spaces_len):
                    if "*" in spaces_array[j]:
                        spaces_array[j] = spaces_array[j].upper().strip()
                        mapping = "\"" + spaces_array[j] + "\" -> \"" + c_code + "\""
                        #write_to_file(mapping)
                        #print(mapping)

    if "one of" or "two of" in preq_str.lower():
        print(preq_str)
        
def read_courses():
    f = open('uvic_courses.json')
    
    # Loading json file
    courses = json.load(f)
    
    
    # For loop to go through courses
    for course in courses:
        course_code_list = list(course['cc'])
        cc_length = len(course_code_list)

        course_code_list.insert(cc_length - 3, "*")
        course_code = "".join(course_code_list)

        # Exit for loop if course is not in desired subject
        #if subject not in course_code:
        #    break

        # Storing course info
        course_desc = course['desc']
        req_string = course['all_preq']

        # If course has no pre-requisites
        #if req_string == "":
            #write_to_file(course_code)

        req_string = req_string.strip()
        if(req_string != ""):
            req_type = type_find(req_string, course_code)

        # Dealing with "mand" types
        # if reqType == "mand" :
        #     #print(reqName)

        #     # Dealing with credit pre-requisites
        #     if "credit" in reqName:

        #         # Deciding not to graph if they do not specify credits in what, may change.

        #         if " in " in reqName:
        #             # Creating string
        #             graphString = "\"" + reqName + "\" -> \"" + course['cc'] + "\""
        #             temp = graphString.split(">")
        #             temp[0] += ">"
        #             if(temp not in courses_list):
        #                 courses_list.append(temp)
        #             #print(graphString)

        #             #splitName = reqName.split(" in ")
                    
        #     else:
        #         # Removing unnecessary brackets
        #         reqName = reqName.replace("(", "")
        #         reqName = reqName.replace(")", "")
        #         reqName = reqName.replace("[", "")
        #         reqName = reqName.replace("]", "")

        #         numCourses = reqName.count("*")
                
        #         # If more than 1 course is present
        #         if numCourses > 1:
        #             #print(reqName)

        #             courseString = reqName.split(" ")

        #             # Looping through text
        #             for i in range(0, len(courseString)) :
        #                 if "*" in courseString[i]:
        #                     # Creating string
        #                     graphString = "\"" + courseString[i] + "\" -> \"" + course['cc'] + "\" [style=solid]"
        #                     temp = graphString.split(">")
        #                     temp[0] += ">"
        #                     if(temp not in courses_list):
        #                         courses_list.append(temp)
        #                     #print(graphString)

        #         else:
        #             # Creating string
        #             graphString = "\"" + reqName + "\" -> \"" + course['cc'] + "\" [style=solid]"
        #             temp = graphString.split(">")
        #             temp[0] += ">"
        #             if(temp not in courses_list):
        #                 courses_list.append(temp)
        #             #print(graphString)
        
        # elif reqType == "or":
        #     if "OR" in reqType:
        #         reqType.replace("OR", "or")
        #     #print(reqName)

        #     if "including" in reqName:
        #         splitIncluding = reqName.split(" including ")

        #         if len(splitIncluding) > 1:
        #             reqName = splitIncluding[1]
        #         #NEED TO COME BACK FOR ELSE CASE!

        #     # Removing unnecessary brackets
        #     reqName = reqName.replace("(", "")
        #     reqName = reqName.replace(")", "")
        #     reqName = reqName.replace("[", "")
        #     reqName = reqName.replace("]", "")

        #     # Splitting by "or"
        #     splitName = reqName.split(" or ")
        #     numCourses = len(splitName)

        #     # For loop to go through courses
        #     for i in range (0, numCourses):
        #         # Removing excess white spaces
        #         splitName[i] = splitName[i].strip()

        #         lcaseCheck = splitName[i].lower()
        #         if "and" in lcaseCheck and ("*" in lcaseCheck):
        #             splitAnd = splitName[i].split("and")
        #             numCoursesAnd = len(splitAnd)

        #             graphString = "\"" + joinVar + "\" -> \"" + splitName[i] + "\" [style=dashed]"
        #             temp = graphString.split(">")
        #             temp[0] += ">"
        #             if(temp not in courses_list):
        #                 courses_list.append(temp)
        #             #print(graphString)

        #             # Looping through all courses binded by "and"
        #             for i in range (0, numCoursesAnd):
        #                 graphString = "\"" + splitAnd[i].strip() + "\" -> \"" + joinVar + "\" [style=solid]"
        #                 temp = graphString.split(">")
        #                 temp[0] += ">"
        #                 if(temp not in courses_list):
        #                     courses_list.append(temp)
        #                 #print(graphString)

        #             # Updating joinVar info
        #             joinVar.replace(str(joinNum), str(joinNum + 1))
        #             joinNum = joinNum + 1

        #         # Creating string
        #         graphString = "\"" + splitName[i] + "\" -> \"" + course['cc'] + "\" [style=dashed]"
        #         temp = graphString.split(">")
        #         temp[0] += ">"
        #         if(temp not in courses_list):
        #             courses_list.append(temp)
        #         #print(graphString)

        # # Splitting by "numOf" type
        # elif reqType == "numOf":
        #     #print(reqName)

        #     reqName = reqName.replace("(", "")
        #     reqName = reqName.replace(")", "")
        #     reqName = reqName.replace("[", "")
        #     reqName = reqName.replace("]", "")

        #     if " of " in reqName:
        #         splitOf = reqName.split(" of ")
        #         numSplits = len(splitOf)

        #         if "*" in splitOf[1]:
                
        #             # For loop to search through string for "# of" format
        #             for i in range(0, numSplits):

        #                 length = len(splitOf[i])

        #                 # First iteration, extract number
        #                 if i == 0:
        #                     numOf = splitOf[i][length - 1]
                        
        #                 # Otherwise, extract courses
        #                 else:

        #                     # Extracting number for next iteration
        #                     if(i != numSplits - 1):
        #                         coursesOf = splitOf[i]
        #                         coursesOf = coursesOf.split(" ")
        #                         numCoursesOf = len(coursesOf)

        #                         # Looping through courses
        #                         for j in range (0, numCoursesOf):
        #                             # If current word is a course
        #                             if("*" in coursesOf[j]):
        #                                 graphString = "\"" + coursesOf[j] + "\" -> \"" + course['cc'] + "\" [style=dashed] [label=\"" + numOf + " of\"]"
        #                                 temp = graphString.split(">")
        #                                 temp[0] += ">"
        #                                 if(temp not in courses_list):
        #                                     courses_list.append(temp)
        #                                 #print(graphString)
        #                         numOf = splitOf[i][length - 1]

        #                     else:
        #                         coursesOf = splitOf[i]
        #                         coursesOf = coursesOf.split(" ")
        #                         numCoursesOf = len(coursesOf)

        #                         # Looping through courses
        #                         for j in range (0, numCoursesOf):
        #                             # If current word is a course
        #                             if("*" in coursesOf[j]):
        #                                 graphString = "\"" + coursesOf[j] + "\" -> \"" + course['cc'] + "\" [style=dashed] [label=\"" + numOf + " of\"]"
        #                                 temp = graphString.split(">")
        #                                 temp[0] += ">"
        #                                 if(temp not in courses_list):
        #                                     courses_list.append(temp)
        #                                 #print(graphString)
        #     else:
        #         graphString = "\"" + reqName + "\" -> \"" + course['cc'] + "\" [style=solid]"
        #         temp = graphString.split(">")
        #         temp[0] += ">"
        #         if(temp not in courses_list):
        #             courses_list.append(temp)
        #         #print(graphString) 
        # elif reqType == "rec":
        #     #print(reqName)

        #     # Removing unnecessary brackets
        #     reqName = reqName.replace("(", "")
        #     reqName = reqName.replace(")", "")
        #     reqName = reqName.replace("[", "")
        #     reqName = reqName.replace("]", "")

        #     # Splitting string by spaces
        #     splitRec = reqName.strip().split(" ")

        #     graphString = "\"" + splitRec[0] + "\" -> \"" + course['cc'] + "\" [style=solid] [label=\"recommended\"]"
        #     temp = graphString.split(">")
        #     temp[0] += ">"
        #     if(temp not in courses_list):
        #         courses_list.append(temp)
        #     #print(graphString)
    
    #print(courses_list)
    f.close()

    # gathering graphviz input based on input
def getGraphvizInput(user_input):
    
    # first read in the courses and put them into graphviz format
    readCourses()
    
    textFileName = "output.dot"
    
    # clear output file
    open(textFileName, 'w').close()
    
    with open(textFileName, "a") as textFile:
        textFile.write("digraph CourseMap {\n")
    
    if "*" in user_input:
        # course code
        courseStack = []
        courseStack.append(user_input.upper())
        
        for course in courseStack:
            courseStack.pop(0)
            
            for mapping in courses_list:
                # iterate through all the course mappings
                
                if course in mapping[1]:
                    # if course matches the course we're searching for
                    
                    # full graphviz line
                    # print(mapping[0] + mapping[1])
                    
                    # add all of these to a file for graphviz
                    with open(textFileName, "a") as textFile:
                        textFile.write(mapping[0] + mapping[1] + "\n")
                    
                    # add the prerequisite to the stack to search for its prerequisities
                    courseStack.append((re.findall('"([^"]*)"', mapping[0]))[0])
        
    else:
        # course prefix
        prefix = user_input
        

        # writing to DOT file 
        for mapping in courses_list:
            if prefix in mapping[1]:
                with open(textFileName, "a") as textFile:
                    textFile.write(mapping[0] + mapping[1] + "\n")
    
    with open(textFileName, "a") as textFile:
        textFile.write("}\n")
    
    
    
    # checking that course program exists    
    with open(textFileName, "r") as textFile:
        if('->' not in textFile.read()):
            print('empty')
            return -1
    
    
    cmd = "dot -Tpdf " + textFileName + " > output.pdf"
    os.system(cmd)

def main():
    read_courses()

if __name__ == "__main__":
    main()