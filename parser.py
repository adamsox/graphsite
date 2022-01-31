#
# CIS*3760 
# Team 10
# 30 Jan 2022
# Program to parse courses.json file and create a list of GraphViz rules
#

# Importing required objects
import json
import re

f = open('courses.json')

# Loading json file
courses = json.load(f)

# Creating list
courses_list  = []
joinNum = 1
joinVar = "Join" + str(joinNum)


# For loop to go through courses
for course in courses:
    #print(course['cc'])
    
    # Creating array to store pre-requisites
    reqArray = course['preqArr']

    # Going through pre-requisites list
    for req in reqArray:

        # Dictionaries to store pre-requisite information
        reqType = req['type']
        reqName = req['preq']

        # Making sure pre-requisite isn't blank
        if reqName == " ":
            break
        
        # Removing excess white spaces
        reqName = reqName.strip()

        # Dealing with "mand" types
        if reqType == "mand" :
            #print(reqName)

            # Dealing with credit pre-requisites
            if "credit" in reqName:

                # Deciding not to graph if they do not specify credits in what, may change.

                if " in " in reqName:
                    # Creating string
                    graphString = "\"" + reqName + "\" -> \"" + course['cc'] + "\""
                    temp = graphString.split(">")
                    temp[0] += ">"
                    courses_list.append(temp)
                    #print(graphString)

                    #splitName = reqName.split(" in ")
                    
            else:
                # Removing unnecessary brackets
                reqName = reqName.replace("(", "")
                reqName = reqName.replace(")", "")
                reqName = reqName.replace("[", "")
                reqName = reqName.replace("]", "")

                numCourses = reqName.count("*")
                
                # If more than 1 course is present
                if numCourses > 1:
                    #print(reqName)

                    courseString = reqName.split(" ")

                    # Looping through text
                    for i in range(0, len(courseString)) :
                        if "*" in courseString[i]:
                            # Creating string
                            graphString = "\"" + courseString[i] + "\" -> \"" + course['cc'] + "\" [style=solid]"
                            temp = graphString.split(">")
                            temp[0] += ">"
                            courses_list.append(temp)
                            #print(graphString)

                else:
                    # Creating string
                    graphString = "\"" + reqName + "\" -> \"" + course['cc'] + "\" [style=solid]"
                    temp = graphString.split(">")
                    temp[0] += ">"
                    courses_list.append(temp)
                    #print(graphString)
        
        elif reqType == "or":
            if "OR" in reqType:
                reqType.replace("OR", "or")
            #print(reqName)

            if "including" in reqName:
                splitIncluding = reqName.split(" including ")

                if len(splitIncluding) > 1:
                    reqName = splitIncluding[1]
                #NEED TO COME BACK FOR ELSE CASE!

            # Removing unnecessary brackets
            reqName = reqName.replace("(", "")
            reqName = reqName.replace(")", "")
            reqName = reqName.replace("[", "")
            reqName = reqName.replace("]", "")

            # Splitting by "or"
            splitName = reqName.split(" or ")
            numCourses = len(splitName)

            # For loop to go through courses
            for i in range (0, numCourses):
                # Removing excess white spaces
                splitName[i] = splitName[i].strip()

                lcaseCheck = splitName[i].lower()
                if "and" in lcaseCheck and ("*" in lcaseCheck):
                    splitAnd = splitName[i].split("and")
                    numCoursesAnd = len(splitAnd)

                    graphString = "\"" + joinVar + "\" -> \"" + splitName[i] + "\" [style=dashed]"
                    temp = graphString.split(">")
                    temp[0] += ">"
                    courses_list.append(temp)
                    #print(graphString)

                    # Looping through all courses binded by "and"
                    for i in range (0, numCoursesAnd):
                        graphString = "\"" + splitAnd[i].strip() + "\" -> \"" + joinVar + "\" [style=solid]"
                        temp = graphString.split(">")
                        temp[0] += ">"
                        courses_list.append(temp)
                        #print(graphString)

                    # Updating joinVar info
                    joinVar.replace(str(joinNum), str(joinNum + 1))
                    joinNum = joinNum + 1

                # Creating string
                graphString = "\"" + splitName[i] + "\" -> \"" + course['cc'] + "\" [style=dashed]"
                temp = graphString.split(">")
                temp[0] += ">"
                courses_list.append(temp)
                #print(graphString)

        # Splitting by "numOf" type
        elif reqType == "numOf":
            #print(reqName)

            reqName = reqName.replace("(", "")
            reqName = reqName.replace(")", "")
            reqName = reqName.replace("[", "")
            reqName = reqName.replace("]", "")

            if " of " in reqName:
                splitOf = reqName.split(" of ")
                numSplits = len(splitOf)

                if "*" in splitOf[1]:
                
                    # For loop to search through string for "# of" format
                    for i in range(0, numSplits):

                        length = len(splitOf[i])

                        # First iteration, extract number
                        if i == 0:
                            numOf = splitOf[i][length - 1]
                        
                        # Otherwise, extract courses
                        else:

                            # Extracting number for next iteration
                            if(i != numSplits - 1):
                                coursesOf = splitOf[i]
                                coursesOf = coursesOf.split(" ")
                                numCoursesOf = len(coursesOf)

                                # Looping through courses
                                for j in range (0, numCoursesOf):
                                    # If current word is a course
                                    if("*" in coursesOf[j]):
                                        graphString = "\"" + coursesOf[j] + "\" -> \"" + course['cc'] + "\" [style=dashed] [label=\"" + numOf + " of\"]"
                                        temp = graphString.split(">")
                                        temp[0] += ">"
                                        courses_list.append(temp)
                                        #print(graphString)
                                numOf = splitOf[i][length - 1]

                            else:
                                coursesOf = splitOf[i]
                                coursesOf = coursesOf.split(" ")
                                numCoursesOf = len(coursesOf)

                                # Looping through courses
                                for j in range (0, numCoursesOf):
                                    # If current word is a course
                                    if("*" in coursesOf[j]):
                                        graphString = "\"" + coursesOf[j] + "\" -> \"" + course['cc'] + "\" [style=dashed] [label=\"" + numOf + " of\"]"
                                        temp = graphString.split(">")
                                        temp[0] += ">"
                                        courses_list.append(temp)
                                        #print(graphString)
            else:
                graphString = "\"" + reqName + "\" -> \"" + course['cc'] + "\" [style=solid]"
                temp = graphString.split(">")
                temp[0] += ">"
                courses_list.append(temp)
                #print(graphString) 
        elif reqType == "rec":
            #print(reqName)

            # Removing unnecessary brackets
            reqName = reqName.replace("(", "")
            reqName = reqName.replace(")", "")
            reqName = reqName.replace("[", "")
            reqName = reqName.replace("]", "")

            # Splitting string by spaces
            splitRec = reqName.strip().split(" ")

            graphString = "\"" + splitRec[0] + "\" -> \"" + course['cc'] + "\" [style=solid] [label=\"recommended\"]"
            temp = graphString.split(">")
            temp[0] += ">"
            courses_list.append(temp)
            #print(graphString)

#print(courses_list)
f.close()

# gathering graphviz input based on input

# example user input
user_input_example = "CIS" #or "CIS*2750"

textFileName = "output.dot"

# clear output file
open(textFileName, 'w').close()

with open(textFileName, "a") as textFile:
    textFile.write("digraph CourseMap {\n")

if "*" in user_input_example:
    # course code
    courseStack = []
    courseStack.append(user_input_example)
    
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
    prefix = user_input_example
    
    for mapping in courses_list:
        if prefix in mapping[1]:
            with open(textFileName, "a") as textFile:
                textFile.write(mapping[0] + mapping[1] + "\n")

with open(textFileName, "a") as textFile:
    textFile.write("}\n")