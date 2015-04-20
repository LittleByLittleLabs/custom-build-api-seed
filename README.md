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


Instructions for Git Workflow

```
1. Git pull or Git clone repo which you plan to make changes to 

2. Create a branch using (`git checkout -b branchname`)  

3. Make the changes

4. Commit the changes locally

5. Push changes to remote repo (`git push -u origin branchname`)

6. Create Pull Request and send to reviewers

7. Address reviewer comments and merge Pull Request to master 
```

Challenge (due April 17th)

We discussed in class what and how to use Apache Bench (https://www.digitalocean.com/community/tutorials/how-to-use-apachebench-to-do-load-testing-on-an-arch-linux-vps).

Your challenge for this week is to create a report in markdown format callled `load_test.md`. This report should contain a few benchmarks/scenarios which you can perform on your app. If you haven't gotten previous weeks challenge to work, then you can simply clone and run the seed github project for students as you did 3 weeks ago. 

Please provide an explanation for each load test scenario and your justification for why or how you came up with the different values for `-n` & `-c` flags.  You can also try using `ngrok` after you document your tests for `localhost` and explain differences.


Challenge Due (April 25th)

1. Implement a 404.html error page 
```
# todo: implement this template
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
```

2. Implement a `index.html` for your project and make it look pretty.  Use `app/index.html` as an example.

3. Get `vagrant up` working for your project 
