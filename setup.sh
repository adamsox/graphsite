sudo apt-get upgrade
sudo apt-get update

sudo apt install libssl1.0-dev
sudo apt install nodejs-dev
sudo apt install node-gyp
sudo apt install npm

#Python:
sudo apt install python3-venv
sudo -m venv myprojectenv

echo 'wheel and uwsgi'
pip install wheel
pip install uwsgi

echo 'python3-pip'
sudo apt install python3-pip

echo 'npm'
sudo apt install npm

# Setup:
# for http testing
# sudo ufw allow 5000

# Commands Dev:
# python3 myproject.py

#(not sure how to run a command in a child directory from a script)
# ( cd myprojectenv ; uwsgi –socket 0.0.0.0:5000 –protocol=http -w wsgi:app )

mkdir ~/etc/systemd
mkdir ~/etc/systemd/system/
mv myproject.service ~/etc/systemd/system/

# start
# sudo systemctl start myproject
# enable at boot
# sudo systemctl enable myproject
# status
# sudo systemctl status myproject

mkdir ~/etc/nginx/
mkdir ~/etc/nginx/sites-available/

mv myproject ~/etc/nginx/sites-available/

sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled

# error check
# sudo nginx -t

# sudo systemctl restart nginx

sudo ufw allow ‘Nginx Full’

# for http Flask testing
# sudo ufw delete allow 5000

sudo ufw delete allow ‘Nginx HTTP’

# for certificates when domain is setup
# sudo add-apt-repository ppa:certbot/certbot
# sudo apt install python3-certbot-nginx
# sudo certbot –nginx -d <domain_name> -d www.<domain_name>