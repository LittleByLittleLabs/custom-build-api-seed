#!/bin/bash

# install web server dependencies
sudo apt-get update
sudo apt-get -y install python python-virtualenv nginx supervisor

# install application (source location in $1)
mkdir /home/vagrant/students
cp $1/requirements.txt /home/vagrant
cp -R $1/students/* /home/vagrant/students/

# create a virtualenv and install dependencies
virtualenv /home/vagrant/students/venv
source /home/vagrant/students/venv/bin/activate
sudo /home/vagrant/students/venv/bin/pip install -r /home/vagrant/requirements.txt

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

echo Application deployed to http://localhost:5000/
