# W22_CIS3760_Team10

#flask_proj

A simple Flask project that just return a static “hello world” text message, which can be accessed through NGINX at its own URL.
Flask Project is currently being hosted on NGINX @ https://131.104.49.112/

After running the setup script cd to myprojectenv and run:
sudo uwsgi –socket 0.0.0.0:5000 –protocol=http -w wsgi:app
