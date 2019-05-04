```
                              _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [w] : /        \ : |========================|    : /        \ :  [w] :
V___________:|    ()    |: |========REDLINE=========|    :|    ()    |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"                                      
```
# Redline
#### Car Modification Tracking Application

## Local development steps

* Clone repository locally
* Create your virtual environment
```
python3 -m venv /path/to/new/virtual/environment
```
* Start virtual environment
```
source /path/to/new/virtual/environment/bin/activate
```
* Configure your virtual environment with file included in repo
```
pip install -r requirements.txt
```
* Initialize db.sqlite3 database
```
python manage.py migrate
```
* Create database superuser
```
python manage.py createsuperuser
```

* Start server
```
python manage.py runserver
```

## Project Dependencies
#### Taken from requirements.txt

* certifi==2019.3.9
* chardet==3.0.4
* Django==2.1.7
* djangorestframework==3.9.1
* idna==2.8
* pycodestyle==2.5.0
* pytz==2018.9
* requests==2.21.0
* urllib3==1.24.1

## API Registration
#### Create a user account through the API

* Formulate an HTTP request with the following JSON data in the body
```
{
  "username": "testuser",
  "email": "testuser@unh.edu",
  "password": "abc123",
  "first_name": "test",
  "last_name": "user"
}
```
* Make a POST request to `POST /api/v1/user/register`
* You can now authenticate yourself with those credentials to receive your auth token

## API Authenication
#### In order to make requests to API endpoints, you need an auth token

* Make a POST request to `POST '/api/v1/user/auth'` and include username and password key value pairs as JSON in the body of the request
* Place the auth token you receive in the header of each request
```
"Auhorization: Token [auth_token]"
```

## Frontend
#### The frontend utilizes Django's templating language and TemplateViews. Very little JavaScript is used.
#### Pages:
* Login - Form to login
* Register - Form to register
* Dashboard - Home screen once logged in
* Car Detail - Shows specific information on a single car
* New Car - Page to add a new car to your account
* New Task - Page to add a new task to a car
* New Part - Page to add a new part to a task
* Edit Task - Page to edit an existing task
* Edit Car - Page to edit an existing Car
* Edit Part - Page to edit an existing part

#### Instructions
* To see the frontend, start server
```
python manage.py runserver
```
* Navigate to `127.0.0.1:8000/` in a browser
* You will be directed to a login page
* If you do not have a login, click the link to register an account
* Once logged in, you have access to all the views

## Endpoints
### Car Endpoint
* This endpoint holds all of the information for the cars owned by a user.
* Required data for the user to enter: ("vin", "year", "make", "model", "color")
* You are able to create a new car, update an existing car's information, get the information for your cars, and delete your cars.
* Endpoint URLs:
* api/ cars/ [name='cars']
* api/ car/<id> [name='car']

### Part Endpoint
* This endpoint holds all the information about the parts needed for tasks.
* Required data for the user to enter: ("name", "price", "quantity")
* You are able to create a new part, update an existing part's information, get the information for the parts, and delete the parts.
* Endpoint URLs:
* api/ parts/ [name='parts']
* api/ part/<id> [name='part']

### Task Endpoint
* This endpoint holds all of the information for each task needed to be performed on the cars.
* Required data for the user to enter: ( "name", "estimated_hours", "due_date", "completion_date", "notes")
* You are able to create a new task, update an existing task's information, get the information for your tasks, and delete your tasks.
* Endpoint URLs:
* api/ car/<id>/tasks/ [name='tasks']
* api/ task/<id> [name='task']

### User Endpoint
* This endpoint holds all of the information for the user who can own cars.
* Required data for the user to enter: ("username", "email", "password", "first_name", "last_name")
* You are able to create a new user and login as that user. each user is able to see all of the cars, tasks, and parts they have. As the user, you are able to create, read, update, and delete as needed.
* Endpoint URLs:
* api/ user/
