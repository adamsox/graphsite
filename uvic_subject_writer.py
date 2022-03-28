#
# Author: Team 10
# Course: CIS*3760
# Date: 28 Mar 2022
# Description: a library to create a json file used to graph given a subject for UVIC
#

import json
import re
import os

nodes_list = []
edges_list = []
visited_list = []

num_of_counter = 0

# Main function
def main():
    print("Please enter subject name: ")
    response = input()
    code_format(response)

# Function to select node colour
def get_color(node_name):
    
    # Initializing color
    color = "#FFFFFF"

    if('*' in node_name):
        index_ast = node_name.index("*")
        course_year = node_name[index_ast + 1]

        # Assigning colour for each year
        if(course_year == '0'):
            color = "#FFC5C5"
        if(course_year == '1'):
            color = "#CEFF58"
        elif(course_year == '2'):
            color = "#6CFF58"
        elif(course_year == '3'):
            color = "#58FF86"
        elif(course_year == '4'):
            color = "#58FFD4"
        elif(course_year == '5'):
            color = "#58D7FF"
        elif(course_year == '6'):
            color = "#588DFF"
        elif(course_year == '7'):
            color = "#7B58FF"

    # Assigning colour for "or" nodes
    elif("OR" in node_name):
        color = "#FFA100"

    # Assigning colour for "# of" nodes
    elif("of" in node_name):
        color = "#FF00F7"

    # Assigning colour for "and" nodes
    elif("AND" in node_name):
        color = "#FF0000"
    
    # Assigning colour for remaining nodes
    else:
        color = "#FF8932"
    
    # Returning colour
    return color

# Function to add a node to the node list
def add_node(node_id, node_name):
    # Getting colour based on node name
    color = get_color(node_name)

    # Creating node dictionary
    node_dict = { "id": node_id, "label": node_name, "color": color }

    # Checking to see if node is in list already before adding it
    if(node_dict not in nodes_list):
        nodes_list.append(node_dict)

# Function to add an edge
def add_edge(node1, node2):
    # Creating edge dictionary
    edge_dict = { "from": node2, "to": node1 }

    # Checking to see if edge is in list already before adding it
    if(edge_dict not in edges_list):
        edges_list.append(edge_dict)

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
    global num_of_counter
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
                num_of_counter = num_of_counter + 1
                id_num_of = "NumOf " + str(num_of_counter)
                add_node(id_num_of, "1 of")
                add_edge(c_code, id_num_of)

                one_of_marker = 1
                two_of_marker = 0
                three_of_marker = 0
                five_of_marker = 0
                all_of_marker = 0
                i+=1
        # If we find "two of" type
        if array_spaces[i].lower() == "two":
            if array_spaces[i + 1].lower() == "of":
                num_of_counter = num_of_counter + 1
                id_num_of = "NumOf " + str(num_of_counter)
                add_node(id_num_of, "2 of")
                add_edge(c_code, id_num_of)

                two_of_marker = 1
                all_of_marker = 0
                one_of_marker = 0
                three_of_marker = 0
                five_of_marker = 0
                i+=1

        # If we find "three of" type
        if array_spaces[i].lower() == "three":
            if array_spaces[i + 1].lower() == "of":
                num_of_counter = num_of_counter + 1
                id_num_of = "NumOf " + str(num_of_counter)
                add_node(id_num_of, "3 of")
                add_edge(c_code, id_num_of)

                three_of_marker = 1
                all_of_marker = 0
                one_of_marker = 0
                two_of_marker = 0
                five_of_marker = 0
                i+=1
        
        # If we find "five of" type
        if array_spaces[i].lower() == "five":
            if array_spaces[i + 1].lower() == "of":
                num_of_counter = num_of_counter + 1
                id_num_of = "NumOf " + str(num_of_counter)
                add_node(id_num_of, "5 of")
                add_edge(c_code, id_num_of)

                five_of_marker = 1
                all_of_marker = 0
                one_of_marker = 0
                two_of_marker = 0
                three_of_marker = 0
                i+=1
        
        # Adding node to list if we are dealing with valid course
        if(array_spaces[i] != "" and "*" in array_spaces[i]):
            add_node(array_spaces[i], array_spaces[i])

        # Dealing with "all of"
        if all_of_marker == 1:
            if "*" in array_spaces[i]:
                add_edge(c_code, array_spaces[i])

        # Dealing with "num of"
        elif one_of_marker == 1 or two_of_marker == 1 or three_of_marker == 1 or five_of_marker == 1:
            if "*" in array_spaces[i]:
                add_edge(id_num_of, array_spaces[i])

        else:
            if "*" in array_spaces[i]:
                add_edge(c_code, array_spaces[i])

        # Incrementing counter
        i+=1

        # Break if we are at end of string
        if i == num_splits:
            finished = 1

def read_courses(subject):
    f = open('uvic_courses.json')
    
    # Loading json file
    courses = json.load(f)
    
    # For loop to go through courses
    for course in courses:
        # Making sure we are not repeating a course
        if course['cc'] in visited_list:
            continue
        else:
            visited_list.append(course['cc'])

        course_code_list = list(course['cc'])
        cc_length = len(course_code_list)

        course_code_list.insert(cc_length - 3, "*")
        course_code = "".join(course_code_list)
        
        # Exit for loop if course is not in desired subject
        if len(subject) != (len(course_code) - 4):
            continue

        if subject.lower() not in course_code.lower():
            continue

        add_node(course_code, course_code)

        # Storing course info
        course_desc = course['desc']
        req_string = course['all_preq']

        req_string = req_string.strip()
        if(req_string != ""):
            type_find(req_string, course_code)

    f.close()

# Putting code into correct graphing format
def code_format(user_input):
    
    # Calling read_courses function
    read_courses(user_input)
    
    graphingFile = "uvic_graph_info.json"
    
    # Clear file
    open(graphingFile, 'w').close()
        
    # Writing nodes list to nodes file
    with open(graphingFile, "a") as textFile:
        textFile.write("{\n\t\"nodes\": ")
        json.dump(nodes_list, textFile)
        textFile.write(",\n\t\"edges\": ")
        json.dump(edges_list, textFile)
        textFile.write("\n}")
    
    # Checking that subject exists 
    if not nodes_list:
        print('empty')
        return -1

if __name__ == "__main__":
    main()