# redline-project
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
* Login - Form to login (This works and isn't static)
* Register - Form to register (This works and isn't static)
* Dashboard - Home screen once logged in
* Car Detail - Shows specific information on a single car
* New Car - Page to add a new car to your account
* New Task - Page to add a new task to a car
* New Part - Page to add a new part to a task
* Edit Task - Page to edit an existing task
* Edit Car - (Coming soon)
* Edit Part - (Coming soon)

#### Instructions
* To see the frontend, start server
```
python manage.py runserver
```
* Navigate to `127.0.0.1:8000/` in a browser
* You will be directed to a login page
* If you do not have a login, click the link to register an account
* Once logged in, you have access to all the views
