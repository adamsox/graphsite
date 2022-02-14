#
# Author: Team 10
# Course: CIS*3760
# Date: 13 Feb 2022
# Description: a library to create a graph(viz) file containing
#              graphs of each subject
#

import json
import re
import os

try:
    os.mkdir("CourseGraphs")
except FileExistsError:
    pass
    
# Function used to write each mapping to its corresponding DOT file
def write_to_file(mapping, text_file_name):

    # If mapping is already found in text file, exit
    with open((text_file_name), "r") as text_file:
        if mapping in text_file.read():
            return 0

    with open((text_file_name), "a") as text_file:
        text_file.write(mapping + "\n")

def fix_course_codes(preq_str):
    word_array = preq_str.split(" ")
    size = len(word_array)
    final_str = ""

    # Going through each word in description
    for i in range(0, size):
        word_array[i] = word_array[i].strip()
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
def type_find(preq_str, c_code, text_file_name):
    preq_str = fix_course_codes(preq_str)

    # Initializing flags
    finished = 0
    array_spaces = preq_str.split(" ")
    num_splits = len(array_spaces)
    i = 0
    all_of_marker = 0
    one_of_marker = 0
    two_of_marker = 0
    three_of_marker = 0
    five_of_marker = 0

    while finished == 0:

        # If we find "all of" type
        if array_spaces[i].lower() == "all":
            if array_spaces[i + 1].lower() == "of":
                all_of_marker = 1
                one_of_marker = 0
                two_of_marker = 0
                three_of_marker = 0
                five_of_marker = 0
                i+=1

        # If we find "one of" type
        if array_spaces[i].lower() == "one":
            if array_spaces[i + 1].lower() == "of":
                one_of_marker = 1
                two_of_marker = 0
                three_of_marker = 0
                five_of_marker = 0
                all_of_marker = 0
                i+=1
        # If we find "two of" type
        if array_spaces[i].lower() == "two":
            if array_spaces[i + 1].lower() == "of":
                two_of_marker = 1
                all_of_marker = 0
                one_of_marker = 0
                three_of_marker = 0
                five_of_marker = 0
                i+=1

        # If we find "three of" type
        if array_spaces[i].lower() == "three":
            if array_spaces[i + 1].lower() == "of":
                three_of_marker = 1
                all_of_marker = 0
                one_of_marker = 0
                two_of_marker = 0
                five_of_marker = 0
                i+=1
        
        # If we find "five of" type
        if array_spaces[i].lower() == "five":
            if array_spaces[i + 1].lower() == "of":
                five_of_marker = 1
                all_of_marker = 0
                one_of_marker = 0
                two_of_marker = 0
                three_of_marker = 0
                i+=1
        
        # Dealing with "all of"
        if all_of_marker == 1:
            if "*" in array_spaces[i]:
                mapping = "\"" + array_spaces[i] + "\" -> \"" + c_code + "\""
                write_to_file(mapping, text_file_name)
                #print(mapping)
        # Dealing with "one of"
        elif one_of_marker == 1:
            if "*" in array_spaces[i]:
                mapping = "\"" + array_spaces[i] + "\" -> \"" + c_code + "\" [style=dashed] [label=\"1 of\", fontcolor=firebrick4] [color=red3]"
                write_to_file(mapping, text_file_name)
                #print(mapping)
        # Dealing with "two of"
        elif two_of_marker == 1:
            if "*" in array_spaces[i]:
                mapping = "\"" + array_spaces[i] + "\" -> \"" + c_code + "\" [style=dashed] [label=\"2 of\", fontcolor=darkgreen] [color=green3]"
                write_to_file(mapping, text_file_name)
                #print(mapping)
        # Dealing with "three of"
        elif three_of_marker == 1:
            if "*" in array_spaces[i]:
                mapping = "\"" + array_spaces[i] + "\" -> \"" + c_code + "\" [style=dashed] [label=\"3 of\", fontcolor=blue4] [color=blue1]"
                write_to_file(mapping, text_file_name)
                #print(mapping)
        # Dealing with "five of"
        elif five_of_marker == 1:
            if "*" in array_spaces[i]:
                mapping = "\"" + array_spaces[i] + "\" -> \"" + c_code + "\" [style=dashed] [label=\"5 of\", fontcolor=maroon4] [color=\"purple3\"]"
                write_to_file(mapping, text_file_name)
                #print(mapping)
        else:
            if "*" in array_spaces[i]:
                mapping = "\"" + array_spaces[i] + "\" -> \"" + c_code + "\" [style=solid]"
                write_to_file(mapping, text_file_name)
                #print(mapping)

            if "*" not in preq_str:
                preq_str = preq_str.strip()
                mapping = "\"" + preq_str + "\" -> \"" + c_code + "\" [style=solid]"
                write_to_file(mapping, text_file_name)

        # Incrementing counter
        i+=1

        # Break if we are at end of string
        if i == num_splits:
            finished = 1


def read_courses(subject):
    f = open('ubc_courses.json')
    
    # Loading json file
    courses = json.load(f)

    text_file_name = "CourseGraphs/" + subject + ".dot"

    # clear output file
    open(text_file_name, 'w').close()

    with open(text_file_name, "a") as text_file:
        text_file.write("digraph " + subject + " {\n")

        # title
        text_file.write("labelloc = \"t\";\nlabel = \""+ subject + "\"\nfontsize = 27;\n")
    
    
    # For loop to go through courses
    for course in courses:
        course_code_list = list(course['cc'])
        cc_length = len(course_code_list)

        course_code_list.insert(cc_length - 3, "*")
        course_code = "".join(course_code_list)
        
        # Exit for loop if course is not in desired subject
        if len(subject) != (len(course_code) - 4):
            continue

        if subject.lower() not in course_code.lower():
            continue

        # Storing course info
        course_desc = course['desc']
        req_string = course['all_preq']

        # If course has no pre-requisites
        if req_string == "":
            write_to_file("\"" + course_code + "\"", text_file_name)

        req_string = req_string.strip()
        if(req_string != ""):
            req_type = type_find(req_string, course_code, text_file_name)
    
    with open(text_file_name, "a") as text_file:
        text_file.write("}\n")

    # Graphing command
    cmd = "dot -Tpdf " + text_file_name + " > CourseGraphs/" + subject + ".pdf"
    os.system(cmd)

    f.close()

def get_subject():
    subject_list = []
    f = open('ubc_courses.json')
    
    # Loading json file
    courses = json.load(f)

    # Extracting subjects from course list
    for course in courses:
        c_code = course['cc']
        if len(c_code) == 5:
            subject = c_code[0] + c_code[1]
        elif len(course['cc']) == 6:
            subject = c_code[0] + c_code[1] + c_code[2]
        elif len(course['cc']) == 7:
            subject = c_code[0] + c_code[1] + c_code[2] + c_code[3]

        # Adding subject to list
        if subject not in subject_list:
            subject_list.append(subject)

    # Passing each subject to read_courses function
    for subj in subject_list:
        read_courses(subj)

    f.close()

def main():
    get_subject()

    # Combining all pdfs into a single pdf
    cmd = "pdftk CourseGraphs/*.pdf cat output merged_courses.pdf"
    os.system(cmd)

if __name__ == "__main__":
    main()
