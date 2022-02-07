# W22_CIS3760_Team10

# scraper.js

Functionality:
    - a javascript application that scrapes all undergraduate course data from all programs 
        offered at the University of Guelph
    - starts by scraping the URLs to each program then scraping the courses from each of those URLs
    - creates "courses.json" file that makes pulling data very easy

Requirements:
    - OS that is supported by playwright e.g. Windows, MacOS, Ubuntu 
    - Node.js and npm installed 
    - all package.json dependencies installed
    - an internet connection for creating http request 

Instructions: 
    - in your command line run the command "npm install" to install dependencies
    - then simply run "node scraper.js" this should create a "courses.json" file

Limitations:
    - courses are scraped from https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/
    - takes some time to run 

Assumptions:
    - User is using a playwright supported OS (we are not using docker)
    - uoguelph website has not changed since having links for each program 
        and courses within those links

# program_scrape.js

Functionality:
    - a javascript application that scrapes all undergraduate majors offered at the University of Guelph
    - starts by scraping the URLs to each degree then scraping the programs (majors) from each of those URLs
    - creates "programs.json" file that makes pulling data very easy

Requirements:
    - OS that is supported by playwright e.g. Windows, MacOS, Ubuntu 
    - Node.js and npm installed 
    - all package.json dependencies installed
    - an internet connection for creating http request 

Instructions: 
    - in your command line run the command "npm install" to install dependencies
    - then simply run "node program_scrape.js" this should create a "programs.json" file

Limitations:
    - courses are scraped from https://calendar.uoguelph.ca/undergraduate-calendar/degree-programs/
    - takes some time to run 

Assumptions:
    - User is using a playwright supported OS (we are not using docker)
    - uoguelph website has not changed since having links for each program 
        and courses within those links

# cli.py

Functionality: 
    - a python script that presents a Command Line Interface that allows users to:

- search for courses, which would be  based on the course code, year, weight, and time it is offered.
- enter a specific undergraduate course code (e.g. CIS*2750), or a general course prefix (e.g. CIS) and have those courses mapped out using GraphViz, with lines connecting them to their pre-requisites. 
- enter an undergraduate major code (e.g. CS), and have all of the required courses in that major mapped out using GraphViz, with lines connecting courses to their pre-requisites.

Requirements:
    - "courses.json" data file
    - "programs.json" data file
    - "course_searcher.py" for searching through courses based on input critera
    - "course_graphviz_writer.py" for creating the graphviz data for courses
    - "major_graphviz_writer.py" for creating the graphviz data for majors
    - python 3

Instructions:
    - Simply run "python cli.py" in your command line

    - To perform a course search, enter "coursesearch <course_code> <course_year> <credit_count> <season>", with "x" representing any field you wish to leave blank. Output will be printed in the terminal.

    - To perform a graphing of course code/prefix, enter "makecoursegraph <course prefix/code>" Output will be printed in the "output.pdf" file.

    - To perform a graphing of majors, enter "makemajorgraph <major code>" Output will be printed in the "output.pdf" file.

    - to exit simply use keywords 'exit', 'quit', or 'q' 

Limitations:
    - user must enter something for all parameters for coursesearch
    - user must enter correct major code for major graphing (and not the name)

Assumptions:
    - user has successfully run "scraper.js" successfully at least once  & has the 'courses.json' file before using the CLI
    - user has successfully run "program_scrape.js" successfully at least once  & has the 'programs.json' file before trying to map the majors
    - data is pulled from "courses.json" and "programs.json"

#gui.py
Functionality: 
    - a python script that presents a Graphical User Interface which is offered as a more user-friendly, bonus alternative to the Command Line Interface (cli.py). This allows users to:
    - search for courses, which would be based on:
        course code, year, weight, and time it is offered

    - enter a specific undergraduate course code (e.g. CIS*2750), or a general course prefix (e.g. CIS) and have those courses mapped out using GraphViz, with lines connecting them to their pre-requisites. 
    
    - enter an undergraduate major code (e.g. CS), and have all of the required courses in that major mapped out using GraphViz, with lines connecting courses to their pre-requisites.

Requirements:
    - "courses.json" data file
    - "programs.json" data file
    - "course_searcher.py" for searching through courses based on input critera
    - "course_graphviz_writer.py" for creating the graphviz data for courses
    - "major_graphviz_writer.py" for creating the graphviz data for majors
    - python 3

Instructions:
    - Simply run "python gui.py" in your command line

    - To perform a course search, click "coursesearch", and enter your desired parameters in the textfields (you may also leave any of them blank). Output will be printed to the terminal.
    
    - To do any graph mappings, click "Graphiz" 
        - To perform a graphing of course code/prefix, click "Make Course Graph" and enter the desired course prefix/code to the textfield. Output will be printed in the "output.pdf" file.
        - To perform a graphing of majors, click "Make Major Graph" and enter the desired major code to the textfield. Output will be printed in the "output.pdf" file.

    - To return home, simply click the "Return Home" button.

    - To exit the program, simply click the "Exit" button.

Limitations:
    - user must enter correct major code for major graphing (and not the name)

Assumptions:
    - user has successfully run "scraper.js" successfully at least once  & has the 'courses.json' file before using the CLI
    - user has successfully run "program_scrape.js" successfully at least once  & has the 'programs.json' file before trying to map the majors
    - data is pulled from "courses.json" and "programs.json"


