#
# Author: Team 10
# Course: CIS*3760
# Date: 26 Mar 2022
# Description: a library to create a json file used to graph given a subject
#

import json
import re
import os

nodes_list = []
edges_list = []

orCounter = 0
andCounter = 0
numOfCounter = 0

# Main function
def main():
    print("Please enter subject name: ")
    response = input()
    codeFormat(response)

# Function to select node colour
def getColor(nodeName):
    
    # Initializing color
    color = "#FFFFFF"

    # If node is a course code
    if('*' in nodeName):
        indexAst = nodeName.index("*")
        courseYear = nodeName[indexAst + 1]

        # Assigning colour for each year
        if(courseYear == '1'):
            color = "#CEFF58"
        elif(courseYear == '2'):
            color = "#63FF58"
        elif(courseYear == '3'):
            color = "#58FFDE"
        elif(courseYear == '4'):
            color = "#5872FF"

    # Assigning colour for "or" nodes
    elif("OR" in nodeName):
        color = "#FFA100"

    # Assigning colour for "# of" nodes
    elif("of" in nodeName):
        color = "#FF00F7"

    # Assigning colour for "and" nodes
    elif("AND" in nodeName):
        color = "#FF0000"
    
    # Assigning colour for remaining nodes
    else:
        color = "#FF8932"
    
    # Returning colour
    return color

# Function to add a node to the node list
def addNode(nodeId, nodeName):
    # Getting colour based on node name
    color = getColor(nodeName)

    # Creating node dictionary
    nodeDict = { "id": nodeId, "label": nodeName, "color": color }

    # Checking to see if node is in list already before adding it
    if(nodeDict not in nodes_list):
        nodes_list.append(nodeDict)

# Function to add an edge
def addEdge(node1, node2):
    # Creating edge dictionary
    edgeDict = { "from": node2, "to": node1 }

    # Checking to see if edge is in list already before adding it
    if(edgeDict not in edges_list):
        edges_list.append(edgeDict)

# Function to read courses from json file
def readCourses(user_input):
    # Opening and loading json file
    f = open('courses.json')
    courses = json.load(f)
    
    # For loop to go through courses
    for course in courses:
        # If course code does not match what user is looking for, continue to next iteration
        if user_input not in course['cc']:
            continue
        
        # Adding course node
        addNode(course['cc'], course['cc'])
        
        # Creating array to store pre-requisites
        reqArray = course['preqArr']
    
        # Going through pre-requisites list
        for req in reqArray:
    
            # Dictionaries to store pre-requisite information
            reqType = req['type']
            reqName = req['preq']
    
            # Making sure pre-requisite isn't blank
            if reqName == " ":
                continue
            
            # Removing excess white spaces
            reqName = reqName.strip()
    
            # Dealing with "mand" types
            if reqType == "mand" :
                # Dealing with credit pre-requisites
                if "credit" in reqName:
    
                    # Graphing if they specify what the credits must be in
                    if " in " in reqName:
                        # Adding edge
                        addEdge(course['cc'], reqName)
                        
                else:
                    # Removing unnecessary brackets
                    reqName = reqName.replace("(", "")
                    reqName = reqName.replace(")", "")
                    reqName = reqName.replace("[", "")
                    reqName = reqName.replace("]", "")

                    numCourses = reqName.count("*")
                    
                    # If more than 1 course is present
                    if numCourses > 1:
                        courseString = reqName.split(" ")
    
                        # Looping through text
                        for i in range(0, len(courseString)) :
                            if "*" in courseString[i]:
                                addEdge(course['cc'], courseString[i])
                    
                    else:
                        # Getting rid of words that are not courses
                        sepSpaces = reqName.split(" ")
                        numWords = len(sepSpaces)

                        if(numWords == 1):
                            addEdge(course['cc'], reqName)
                        else:
                            for i in range(0, numWords):
                                if "*" in sepSpaces[i]:
                                    addEdge(course['cc'], sepSpaces[i])

            # Dealing with "Or" types
            elif reqType == "or":
                # Incrementing "or" counter and assigning ID
                global orCounter 
                orCounter = orCounter + 1
                idOr = "Or " + str(orCounter)

                # Converting to lowercase
                if "OR" in reqType:
                    reqType.replace("OR", "or")

                # If "including" is involved
                if "including" in reqName:
                    splitIncluding = reqName.split("including ")
    
                    if len(splitIncluding) > 1:
                        reqName = splitIncluding[1]
    
                # Removing unnecessary brackets
                reqName = reqName.replace("(", "")
                reqName = reqName.replace(")", "")
                reqName = reqName.replace("[", "")
                reqName = reqName.replace("]", "")
    
                # Splitting by "or"
                splitName = reqName.split(" or ")
                numCourses = len(splitName)

                # Creating link from "OR" node to course node
                addNode(idOr, "OR")
                addEdge(course['cc'], idOr)

                # For loop to go through courses in "or"
                for i in range (0, numCourses):
                    # Removing excess white spaces
                    splitName[i] = splitName[i].strip()

                    # Checking to see if "and" is present
                    lcaseCheck = splitName[i].lower()
                    if ("and" in lcaseCheck) and ("*" in lcaseCheck):
                        # Incrementing "and" counter and assigning ID
                        global andCounter
                        splitAnd = splitName[i].split("and")
                        numCoursesAnd = len(splitAnd)
                        andCounter = andCounter + 1
                        idAnd = "And " + str(andCounter)

                        addNode(idAnd, "AND")
                        addEdge(idOr, idAnd)
    
                        # Looping through all courses binded by "and"
                        for i in range (0, numCoursesAnd):
                            addNode(splitAnd[i].strip(), splitAnd[i].strip())
                            addEdge(idAnd, splitAnd[i].strip())
                    
                    # If "and" is not present
                    else:
                        addNode(splitName[i], splitName[i])
                        addEdge(idOr, splitName[i])
    
            # Splitting by "numOf" type
            elif reqType == "numOf":
                global numOfCounter
    
                reqName = reqName.replace("(", "")
                reqName = reqName.replace(")", "")
                reqName = reqName.replace("[", "")
                reqName = reqName.replace("]", "")
    
                if " of " in reqName:
                    splitOf = reqName.split(" of ")
                    numSplits = len(splitOf)

                    # If dealing with courses
                    if "*" in splitOf[1]:
                        # For loop to search through string for "# of" format
                        for i in range(0, numSplits):
                            length = len(splitOf[i])
    
                            # First iteration, extract number
                            if i == 0:
                                # Getting number
                                numOf = splitOf[i][length - 1]
                                numOfStr = str(numOf) + " of"

                                # Adding node for "# of"
                                numOfCounter = numOfCounter + 1
                                idNumOf = "NumOf " + str(numOfCounter)

                                addNode(idNumOf, numOfStr)
                                addEdge(course['cc'], idNumOf)
                            
                            # Otherwise, extract courses
                            else:
                                # If number if specified
                                if(numOf.isdigit() == True):
                                    # Splitting up sentences into courses
                                    coursesOf = splitOf[i]
                                    coursesOf = coursesOf.split(" ")
                                    numCoursesOf = len(coursesOf)
    
                                    # Looping through courses
                                    for j in range (0, numCoursesOf):
                                        # If current word is a course
                                        if("*" in coursesOf[j]):
                                            addNode(coursesOf[j], coursesOf[j])
                                            addEdge(idNumOf, coursesOf[j])

                                    # If it is not last numOf in sentence
                                    if(i != numSplits - 1):
                                        # Getting new number for numOf
                                        numOf = splitOf[i][length - 1]
                                        numOfStr = str(numOf) + " of"

                                        # Adding node for "# of"
                                        numOfCounter = numOfCounter + 1
                                        idNumOf = "NumOf " + str(numOfCounter)

                                        addNode(idNumOf, numOfStr)
                                        addEdge(course['cc'], idNumOf)

                                # If it is not a "number of"
                                else:
                                    # Splitting up sentence by spaces
                                    strOf = splitOf[1].split(" ")
                                    numStrOf = len(strOf)

                                    # For loop to traverse through each word
                                    for j in range(0, numStrOf):
                                        # If current word is a course
                                        if "*" in strOf[j]:
                                            addNode(strOf[j], strOf[j])
                                            addEdge(course['cc'], strOf[j])
                # Special cases
                else:
                    # Making sure "of" is in sentence
                    if("of" in reqName.lower()):
                        if("OF" in reqName):
                            reqName = reqName.replace("OF", "of")
                    
                    # Splitting by "of"
                    splitOf = reqName.split("of")

                    strLength = len(splitOf[0])
                    numOf = splitOf[0][strLength - 1]

                    numOfStr = str(numOf) + " of"

                    # Adding node for "# of"
                    numOfCounter = numOfCounter + 1
                    idNumOf = "NumOf " + str(numOfCounter)

                    addNode(idNumOf, numOfStr)
                    addEdge(course['cc'], idNumOf)

                    coursesOf = splitOf[i]
                    coursesOf = coursesOf.split(" ")
                    numCoursesOf = len(coursesOf)

                    # Looping through courses
                    for j in range (0, numCoursesOf):
                    # If current word is a course
                        if("*" in coursesOf[j]):
                            # Adding node
                            addNode(coursesOf[j], coursesOf[j])
                            addEdge(idNumOf, coursesOf[j])
    
    json_string = json.dumps(nodes_list)
    f.close()

# Putting code into correct graphing format
def codeFormat(user_input):
    
    # Calling readCourses function
    readCourses(user_input)
    
    graphingFile = "graph_info.json"
    nodesFile = "nodes.json"
    edgesFile = "edges.json"
    
    # Clear files
    open(graphingFile, 'w').close()
        
    # Writing nodes list to nodes file
    with open(graphingFile, "a") as textFile:
        textFile.write("{\n\t\"nodes\": ")
        json.dump(nodes_list, textFile)
        textFile.write(",\n\t\"edges\": ")
        json.dump(edges_list, textFile)
        textFile.write("\n}")
    
    # Writing edges list to edges file
    #with open(edgesFile, "a") as textFile:
    #    json.dump(edges_list, textFile)  
    
    # Checking that subject exists 
    if not nodes_list:
        print('empty')
        return -1

if __name__ == "__main__":
    main()