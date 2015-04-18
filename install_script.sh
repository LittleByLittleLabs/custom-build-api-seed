#!/bin/bash

# install web server dependencies
sudo apt-get update
sudo apt-get -y install python python-virtualenv nginx supervisor

# install application (source location in $1)
mkdir /home/vagrant/student
cp -R $1/student/* /home/vagrant/student/

# create a virtualenv and install dependencies
virtualenv /home/vagrant/student/venv
/home/vagrant/student/venv/bin/pip install -r /home/vagrant/student/requirements.txt

# configure supervisor
sudo cp /vagrant/student.conf /etc/supervisor/conf.d/
sudo mkdir /var/log/student
sudo supervisorctl reread
sudo supervisorctl update

# configure nginx
sudo cp /vagrant/student.nginx /etc/nginx/sites-available/student
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/student /etc/nginx/sites-enabled/
sudo service nginx restart

echo Application deployed to http://192.168.10.11/
