Custom APIs using Flask
=====================

This repo contains a seed project to help you start building a microservice with custom API endpoints.

If this is your first time, do the following after you clone:

```
# create a virtualenv environment
virtualenv venv

# start virtualenv environment 
source venv/bin/activate

# install dependencies needed for your app
pip install -r requirements.txt

# start the server 
python requests/app/api.py

# stop virtualenv environment 
deactivate
```

For subsequent runs, simply do the following:
```
# start virtualenv environment 
source venv/bin/activate

# start the server, ctrl-c if you want to stop server
python requests/app/api.py

# in separate console window, retrieve all students
http GET http://localhost:5000/students/

# in separate console window, create a new student
http POST  http://localhost:5000/students/ name=Armen

# in separate console window, retrieve a specific user
http GET http://localhost:5000/students/1

# stop virtualenv environment when you're finished
deactivate
```
