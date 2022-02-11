#
# Author: Team 10
# Course: CIS*3760
# Date: 7 Feb 2022
# Description: a command-line interface for a user to interact with
#              various features
#

import course_searcher
import course_graphviz_writer
import major_graphviz_writer

def main():
    while True:
        user_input = input().lower()
        arguments = user_input.split()
        
        # handle input edge case
        if "coursesearch" in arguments[0]:
            arguments.pop(0)


        if user_input == "exit" or user_input == "quit" or user_input == "q":
            # exit
            break
        
        elif len(arguments) == 2 and (arguments[0] == "makecoursegraph" or arguments[0] == "makemajorgraph"):
            # make a graph
            ret_val = None
            if arguments[0] == "makecoursegraph":
                # course graph (course_prefix or course_code)
                ret_val = make_graph_course(arguments)
            elif arguments[0] == "makemajorgraph":
                # major graph
                ret_val = make_graph_major(arguments)
                
            if ret_val == -1:
                print("Error while creating graph")
            else:
                print("Graphviz file succesfully created")
                
        elif len(arguments) == 4:
            # search for courses that match a description
            ret_val = search_course(arguments)
            if ret_val == -1:
                print("Error while searching for course code")
            elif ret_val == None:
                print("No courses found that match the description given")
            else: 
                # print courses found
                for course in ret_val:
                    print(str(course['cc']) + " " + str(course['cred']) + " " + str(course['desc']) + " " +  str(course['off']))
            print()
            
        else:
            # if user enters a command other than exit or coursesearch or makegraph
            print("INVALID COMMAND OR NUMBER OF PARAMETERS")
            usageMessage()
            
    return None

def search_course(args_list):
    return course_searcher.search_course(args_list)

# call the Graphviz courseParser
def make_graph_course(args_list):
    return course_graphviz_writer.getGraphvizInput(args_list[1].upper())

def make_graph_major(args_list):
    return major_graphviz_writer.read_major(args_list[1].upper())


def usageMessage():
    print("usage: coursesearch course_code course_year credit_count season")
    print("Put \'x\' for anything you do not wish to specify.")
    print("e.g., 'coursesearch: cis 3 0.75 f' searches for a cis 3rd year 0.75 fall course")
    print("e.g., 'coursesearch: hist x 1.00 x' searches for a hist 1.00 course regardless of year or semester")
    print("or")
    print("usage: makecoursegraph (course prefix or course code)")
    print("or")
    print("usage: makemajorgraph (course prefix or course code)")
    print("or")
    print("usage: exit")


if __name__ == "__main__":
    usageMessage()
    main()
