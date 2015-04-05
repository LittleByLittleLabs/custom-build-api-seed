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

# Test 1: in separate console window, retrieve all students
http GET http://localhost:5000/students/

# Test 2: in separate console window, create a new student
http POST  http://localhost:5000/students/ name=Armen

# Test 3: in separate console window, retrieve a specific user
http GET http://localhost:5000/students/1

# Test 4: in separate console window, update an existing user
http PUT http://localhost:5000/students/1 name="Changed Name"

# stop virtualenv environment when you're finished
deactivate
```

Challenge (due April 5th):
```
1. Complete the `For subsequent runs` section above
2. Write a script which will test the 4 endpoints above (GET, POST, GET, PUT) using curl.
3. Write a script which will populate 30 records into your database. 
```


Challenge (due April 12th)

1. Find a data set

2. Create a SQL schema 

3. Write a script to extract and transform the data into an input file

3. Implement REST POST endpoint to populate data into sqlite

4. Write a script to load data into DB using curl from previous step



Some interesting product feature ideas may be:

Best Posts

Worst Posts

Most Controversial

Most Commented

Most/Least posts by author

Top Site References

**Don't forget to push your github branch on Mondays.
