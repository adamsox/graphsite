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

# cli.py

Functionality: 
    - a python script that presents a Command Line Interface that allows users to search for courses based on:
        course code, year, weight, and time it is offered; or make a graph based on a course prefix or course code

Requirements:
    - "courses.json" data file
    - "courseParser.py" for creating the graphviz data
    - python 3

Instructions:
    - simply run "python cli.py" in your command line and it will prompt you to enter your search parameters
    - to enter parameters correctly, they must use the following order: coursesearch course_code course_year credit_count season
    - if you do not wish to use a certain parameter, enter 'x' to leave it blank
    - or makegraph (course prefix or course code)
    - to exit simply use keywords 'exit', 'quit', or 'q' 

Limitations:
    - user must enter something for all parameters

Assumptions:
    - user has successfully ran the at least once scraper before using the CLI & has the 'courses.json' file
    - data is pulled from "courses.json" 


