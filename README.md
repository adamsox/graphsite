# W22_CIS3760_Team10

A simple flask backend that has a search functionality (functionality imported from previous CLI)
Very basic react front end that consists of a form with a textbox and a button. In the textbox, enter your search parameters e.g. cis x x w, hist x 1.00 x, acct 3 0.5 f.
For a temporary time, users will need to use 'x' to respresent a blank parameter. Ensure you include all 4 parameters in the correct order in order
for search to work (course_code level_year course_weight time_offered). For the time being result data is displayed in JSON format


# Frontend(production)

1. navigate into root of react project and run npm install

2. then run npm start to load the react development server

3. the frontend will open up on a local port

4. once you are satisfied with the changes: npm run build 

5. creates a build folder, bring the build folder over to the server then run 

6. move to folder where nginx will serve build: sudo cp -r /home/sysadmin/Sprint6/build/. /var/www/html


# Frontend(locally)

1. this project run from local can connect to the production backend



# Api


1. to make changes to api modify files in the api/ folder

2. for example modify a route in the myproject.py file

3. sudo systemctl restart myproject.service 



# Endpoints

frontend: http://131.104.49.112/

current time endpoint: http://131.104.49.112/api/time


post coures search : http://131.104.49.112/api/query


# NGINX setup commands

sudo rm /etc/nginx/sites-enabled/default

sudo apt-get install nginx

sudo ln -s /etc/nginx/sites-available/react-flask-app.nginx /etc/nginx/sites-enabled/react-flask-app.nginx

sudo systemctl reload nginx

# Helpful commands (Frontend)

sudo cp -r /home/sysadmin/Sprint6/build/. /var/www/html


# Helpful commands (Backend)
sudo apt-get install nginx

sudo nano /etc/systemd/system/myproject.service

uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app

run npm run build in react root then copy folder to /var/www/html

sudo cp -r /home/sysadmin/Sprint6/build/. /var/www/html

vi myproject.py 

sudo systemctl restart myproject.service

sudo systemctl status myproject

SensesNeighbour



# Helpful Resources

https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units

https://stackoverflow.com/questions/58345210/get-data-from-react-to-flask-via-post

https://vovaprivalov.medium.com/solve-cors-problem-in-flask-rest-api-47250f1c77fa

https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project

https://blog.devgenius.io/using-nginx-to-serve-react-application-static-vs-proxy-69b85f368e6c
