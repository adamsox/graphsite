# W22_CIS3760_Team10

# scraper.js

**Functionality**:
    a javascript application that scrapes all undergraduate course data from all programs 
        offered at the University of Guelph
    starts by scraping the URLs to each program then scraping the courses from each of those URLs
    creates "courses.json" file that makes pulling data very easy

**Requirements**:
- OS that is supported by playwright e.g. Windows, MacOS, Ubuntu 
- Node.js and npm installed 
- All package.json dependencies installed
- An internet connection for creating http request 

**Instructions**: 
- In your command line run the command "npm install" to install dependencies
- Then simply run "node scraper.js" this should create a "courses.json" file

**Limitations**:
- Courses are scraped from https://calendar.uoguelph.ca/undergraduate-calendar/course-descriptions/
- Takes some time to run 

**Assumptions**:
- User is using a playwright supported OS (we are not using docker)
- uoguelph website has not changed since having links for each program 
and courses within those links

# program_scrape.js

**Functionality**:
    A javascript application that scrapes all undergraduate majors offered at the University of Guelph
    It starts by scraping the URLs to each degree then scraping the programs (majors) from each of those URLs
    It creates a "programs.json" file that makes pulling data very easy

**Requirements**:
- OS that is supported by playwright e.g. Windows, MacOS, Ubuntu 
- Node.js and npm installed 
- All package.json dependencies installed
- An internet connection for creating http request 

**Instructions**: 
- In your command line run the command "npm install" to install dependencies
- Then simply run "node program_scrape.js" this should create a "programs.json" file

**Limitations**:
- Courses are scraped from https://calendar.uoguelph.ca/undergraduate-calendar/degree-programs/
- Takes some time to run 

**Assumptions**:
- User is using a playwright supported OS (we are not using docker)
- uoguelph website has not changed since having links for each program 
and courses within those links

# cli.py

**Functionality**: 
    A python script that presents a Command Line Interface that allows users to:

- search for courses, which would be  based on the course code, year, weight, and time it is offered.
- enter a specific undergraduate course code (e.g. CIS*2750), or a general course prefix (e.g. CIS) and have those courses mapped out using GraphViz, with lines connecting them to their pre-requisites. 
- enter an undergraduate major code (e.g. CS), and have all of the required courses in that major mapped out using GraphViz, with lines connecting courses to their pre-requisites.

**Requirements**:
- "courses.json" data file
- "programs.json" data file
- "course_searcher.py" for searching through courses based on input critera
- "course_graphviz_writer.py" for creating the graphviz data for courses
- "major_graphviz_writer.py" for creating the graphviz data for majors
- Python 3

**Instructions**:
- Simply run "python cli.py" in your command line

- To perform a course search, enter "coursesearch <course_code> <course_year> <credit_count> <season>", with "x" representing any field you wish to leave blank. Output will be printed in the terminal.

- To perform a graphing of course code/prefix, enter "makecoursegraph <course prefix/code>" Output will be printed in the "output.pdf" file.

- To perform a graphing of majors, enter "makemajorgraph <major code>" Output will be printed in the "output.pdf" file.

- To exit simply use keywords 'exit', 'quit', or 'q' 

**Limitations**:
- User must enter something for all parameters for coursesearch
- User must enter correct major code for major graphing (and not the name)

**Assumptions**:
- User has successfully run "scraper.js" successfully at least once  & has the 'courses.json' file before using the CLI
- User has successfully run "program_scrape.js" successfully at least once  & has the 'programs.json' file before trying to map the majors
- Data is pulled from "courses.json" and "programs.json"

#gui.py
**Functionality**: 
    A python script that presents a Graphical User Interface which is offered as a more user-friendly, bonus alternative to the Command Line Interface (cli.py). This allows users to:
- Search for courses, which would be based on: course code, year, weight, and time it is offered

- Enter a specific undergraduate course code (e.g. CIS*2750), or a general course prefix (e.g. CIS) and have those courses mapped out using GraphViz, with lines connecting them to their pre-requisites. 
    
- Enter an undergraduate major code (e.g. CS), and have all of the required courses in that major mapped out using GraphViz, with lines connecting courses to their pre-requisites.

**Requirements**:
- "courses.json" data file
- "programs.json" data file
- "course_searcher.py" for searching through courses based on input critera
- "course_graphviz_writer.py" for creating the graphviz data for courses
- "major_graphviz_writer.py" for creating the graphviz data for majors
- Python 3

**Instructions**:
- Simply run "python gui.py" in your command line

- To perform a course search, click "coursesearch", and enter your desired parameters in the textfields (you may also leave any of them blank). Output will be printed to the terminal.
    
- To do any graph mappings, click "Graphiz" 
    - To perform a graphing of course code/prefix, click "Make Course Graph" and enter the desired course prefix/code to the textfield. Output will be printed in the "output.pdf" file.
    - To perform a graphing of majors, click "Make Major Graph" and enter the desired major code to the textfield. Output will be printed in the "output.pdf" file.

- To return home, simply click the "Return Home" button.

- To exit the program, simply click the "Exit" button.

**Limitations**:
    - User must enter correct major code for major graphing (and not the name)

**Assumptions**:
- User has successfully run "scraper.js" successfully at least once  & has the 'courses.json' file before using the CLI
- User has successfully run "program_scrape.js" successfully at least once  & has the 'programs.json' file before trying to map the majors
- Data is pulled from "courses.json" and "programs.json"


