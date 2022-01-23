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

def courseSearch(args_list):

    # case where the only argument is the program name
    if len(args_list) == 1:
        print("usage: coursesearch course_code credit_count season")
        return None
    
    else:
        found = False
        course_code = args_list[1]
        i = 0

        # iterating through the list of courses untill the desired course is found or until it reaches the end of the list
        while not(found) and i < len(courses):
    
            if courses[i]['cc'] == course_code:
                found = True
                print(str(courses[i]['cc']) + " " + str(courses[i]['cred']) + " " + str(courses[i]['desc']) + " " +  str(courses[i]['off']))
            i+=1
        
        if not(found):
            print("no matches found")

    return None


# This function opens the courses.json file and takes its contents
def openCourses():
    with open("courses.json", "r") as file:
        jsonData = json.load(file)

    for i in jsonData:
        courses.append(i)

    return None


if __name__ == "__main__":
    print("Close the program by inputing exit or search for a course by inputing coursesearch.")
    openCourses()
    main()